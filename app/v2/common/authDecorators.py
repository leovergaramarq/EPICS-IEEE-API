from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from flask import jsonify
from v2.models import Role, User


def auth_required(l: list):
    def wraper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims['role'] in l:
                return fn(*args, **kwargs)
            else:
                return {'msg': 'You are not authorized to access this resource'}, 403

        return decorator

    return wraper


def self_allowed():
    def wrapper(fn):
        @wraps(fn)
        def decorator(content, *args, **kwargs):

            verify_jwt_in_request()
            claims = get_jwt()

            username_claims = User.objects.get(username=claims['sub']['username'])
            username_content = User.objects.get(username=content['username'])

            if username_claims == username_content:
                return fn(content, *args, **kwargs)
            else:
                return {'msg': 'Authentication error'}, 403

        return decorator

    return wrapper


def role_permission_required(rel):
    def wraper(fn):
        @wraps(fn)
        def decorator(content, *args, **kwargs):

            try:
                verify_jwt_in_request()
                claims = get_jwt()

                role_claims = Role.objects.get(name=claims['sub']['role'])
                role_content = Role.objects.get(name=content['role'])

                if rel == '>':
                    if role_claims.permission_level < role_content.permission_level:
                        return fn(content, *args, **kwargs)
                    else:
                        return {
                            'msg': 'You are not authorized to access this resource'
                        }, 403

                elif rel == '>=':
                    if role_claims.permission_level <= role_content.permission_level:
                        return fn(content, *args, **kwargs)
                    else:
                        return {
                            'msg': 'You are not authorized to access this resource'
                        }, 403

            except KeyError:
                return {'msg': 'Token\'s role and/or content\'s role not provided'}
            except Role.DoesNotExist:
                return {'msg': 'Invalid role'}

        return decorator

    return wraper


def admin_required(fn):
    @wraps(fn)
    def decorator(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()
        if claims['sub']['role'] == 'admin':
            return fn(*args, **kwargs)
        else:
            return {'msg': 'Admins only!'}, 403

    return decorator


def rector_required(fn):
    @wraps(fn)
    def decorator(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()
        if claims['sub']['role'] == 'rector':
            return fn(*args, **kwargs)
        else:
            return {'msg': 'Admins only!'}, 403

    return decorator


def rector_or_admin_required(fn):
    @wraps(fn)
    def decorator(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()
        print(claims['sub']['role'])
        if claims['sub']['role'] == 'admin' or claims['sub']['role'] == 'rector':
            return fn(*args, **kwargs)
        else:
            return {'msg': 'Admins or Rectors only!'}, 403

    return decorator

def school_member_required(fn):
    @wraps(fn)
    def decorator(id_school, *args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()
        if claims['sub']['role'] == 'admin':
            return fn(id_school, *args, **kwargs)
        else:
            username = claims['sub']['username']
            user = User.objects.get(username=username)
            if user.id_school == id_school:
                return fn(id_school, *args, **kwargs)
            else:
                return {'msg': 'You are not authorized to access this resource'}, 403

    return decorator