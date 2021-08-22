from flask_restful import Resource
from flask import request
from database.commonQueries import get_registers, post_register
from database.specialQueries import getSchools

class School(Resource):
    def get(self):
        return get_registers("school")
    
    def put(self):
        content = request.get_json()
        return post_register("school",content)

class BasicSchool(Resource):
    def get(self):
        return getSchools()