from flask import Blueprint, request
from . import course, game, user, school, professor, admin, rector, student, session_game as session

app = Blueprint('web', __name__)

@app.route('/ping', methods=['GET'])
def root():
    return {'msg': 'Welcome to /v2.0/web'}

# USER ***********************************************
@app.route('/login', methods=['POST'])
def login():
    return user.login(request.get_json())

@app.route('/user')
def get_users():
    return user.get_users()

@app.route('/user/<username>')
def get_user(username):
    return user.get_user(username)

@app.route('/user', methods=['POST'])
def post_user():
    return user.post_user(request.get_json())

@app.route('/user/<username>', methods=['DELETE'])
def delete_user(username):
    return user.delete_user(username)

@app.route('/user/<username>', methods=['PUT'])
def put_user(username):
    return user.put_user(username, request.get_json())

# PROFESSOR ***********************************************
@app.route('/professor', methods=['POST'])
def post_professor():
    return professor.post_professor(request.get_json())

@app.route('/professor/<username>', methods=['PUT'])
def put_professor(username):
    return professor.put_professor(username, request.get_json())

@app.route('/professor/<username>', methods=['DELETE'])
def delete_professor(username):
    return professor.delete_professor(username)

@app.route('/school/<id_school>/professor', methods=['GET'])
def get_school_professors(id_school):
    return professor.get_school_professors(id_school)

@app.route('/school/<id_school>/professor/<username>', methods=['GET'])
def get_school_professor(id_school, username):
    return professor.get_school_professor(id_school, username)

# RECTOR ***********************************************
@app.route('/rector', methods=['POST'])
def post_rector():
    return rector.post_rector(request.get_json())

@app.route('/rector/<username>', methods=['PUT'])
def put_rector(username):
    return rector.put_rector(username, request.get_json())

@app.route('/rector/<username>', methods=['DELETE'])
def delete_rector(username):
    return rector.delete_rector(username)

@app.route('/school/<id_school>/rector', methods=['GET'])
def get_school_rectors(id_school):
    return rector.get_school_rectors(id_school)

# @app.route('/school/<id_school>/rector/<username>', methods=['GET'])
# def get_school_rector(id_school, username):
#     return rector.get_school_rectors(id_school, username)

# STUDENT ***********************************************
@app.route('/student', methods=['POST'])
def post_student():
    return student.post_student(request.get_json())

@app.route('/student/<username>', methods=['PUT'])
def put_student(username):
    return student.put_student(username, request.get_json())

@app.route('/student/<username>', methods=['DELETE'])
def delete_student(username):
    return student.delete_student(username)

@app.route('/school/<id_school>/student', methods=['GET'])
def get_school_students(id_school):
    return student.get_school_students(id_school)

@app.route('/school/<id_school>/course/<course_code>/student', methods=['GET'])
def get_course_students(id_school, course_code):
    return student.get_course_students(id_school, course_code)

# @app.route('/school/<id_school>/student/<username>', methods=['GET'])
# def get_school_student(id_school, username):
#     return student.get_school_students(id_school, username)

# SCHOOL ***********************************************
@app.route('/school')
def get_schools():
    return school.get_schools()

@app.route('/school/<id_school>')
def get_school(id_school):
    return school.get_school(id_school)

@app.route('/school', methods=['POST'])
def post_school():
    return school.post_school(request.get_json())

@app.route('/school/<id_school>', methods=['DELETE'])
def delete_school(id_school):
    return school.delete_school(id_school)

@app.route('/school/<id_school>', methods=['PUT'])
def put_school(id_school):
    return school.put_school(id_school, request.get_json())

# COURSE ***********************************************
@app.route('/school/<id_school>/course')
def get_school_courses(id_school):
    return course.get_school_courses(id_school)

@app.route('/school/<id_school>/course/<course_code>')
def get_school_course(id_school, course_code):
    return course.get_school_course(id_school, course_code)

@app.route('/school/<id_school>/course', methods=['POST'])
def post_course(id_school):
    return course.post_course(id_school, request.get_json())

@app.route('/school/<id_school>/course/<course_code>', methods=['PUT'])
def put_course(id_school, course_code):
    return course.put_course(id_school, course_code, request.get_json())

@app.route('/school/<id_school>/course/<course_code>', methods=['DELETE'])
def delete_course(id_school, course_code):
    return course.delete_course(id_school, course_code)

# # get all games from a course with course id
# @app.route('/school/<id_school>/course/<course_code>/game', methods=['GET'])
# def get_games_from_course(id_school, course_code):
#     return game.get_games_from_course(id_school, course_code)

# # delete all games from a course with course id
# @app.route('/school/<id_school>/course/<course_code>/game', methods=['DELETE'])
# def delete_games_from_course(id_school, course_code):
#     return game.delete_games_from_course(id_school, course_code)

# add an existing game into a course with game id
@app.route('/school/<id_school>/course/<course_code>/game', methods=['POST'])
def add_game_to_course(id_school, course_code):
    return course.add_game_to_course(id_school, course_code, request.get_json())

# delete an existing game from a course with game id
@app.route('/school/<id_school>/course/<course_code>/game/<game_code>', methods=['DELETE'])
def del_game_from_course(id_school, course_code, game_code):
    return course.del_game_from_course(id_school, course_code, game_code)

# add existing games into a course with game id
@app.route('/school/<id_school>/course/<course_code>/games', methods=['POST'])
def add_games_to_course(id_school, course_code):
    return course.add_games_to_course(id_school, course_code, request.get_json())

# delete existing games from a course with game id
@app.route('/school/<id_school>/course/<course_code>/games', methods=['DELETE'])
def del_games_from_course(id_school, course_code):
    return course.del_games_from_course(id_school, course_code, request.args.getlist('code'))

# GAME ***********************************************
@app.route('/school/<id_school>/game')
def get_school_games(id_school):
    return game.get_school_games(id_school)

@app.route('/school/<id_school>/game/<game_code>')
def get_school_game(id_school, game_code):
    return game.get_school_game(id_school, game_code)

@app.route('/school/<id_school>/game', methods=['POST'])
def post_game(id_school):
    return game.post_game(id_school, request.get_json())

@app.route('/school/<id_school>/game/<game_code>', methods=['PUT'])
def put_game(id_school, game_code):
    return game.put_game(id_school, game_code, request.get_json())

@app.route('/school/<id_school>/game/<game_code>', methods=['DELETE'])
def delete_game(id_school, game_code):
    return game.delete_game(id_school, game_code)

# # add an existing game into a course with game id
# @app.route('/school/<id_school>/course/<course_code>/game', methods=['POST'])
# def post_game_into_course(id_school, course_code):
#     return game.post_game_into_course(id_school, course_code)

# # delete an existing game from a course with game id
# @app.route('/school/<id_school>/course/<course_code>/game/<game_code>', methods=['DELETE'])
# def delete_game_from_course(id_school, course_code, game_code):
#     return game.delete_game_from_course(id_school, course_code, game_code)

# # get all games from a course with course id
# @app.route('/school/<id_school>/course/<course_code>/game', methods=['GET'])
# def get_games_from_course(id_school, course_code):
#     return game.get_games_from_course(id_school, course_code)

# # delete all games from a course with course id
# @app.route('/school/<id_school>/course/<course_code>/game', methods=['DELETE'])
# def delete_games_from_course(id_school, course_code):
#     return game.delete_games_from_course(id_school, course_code)
# def delete_game(id_school, code_course, game_code):
#     return game.delete_game(id_school, code_course, game_code)

# # add an existing game into a course with game id
# @app.route('/school/<id_school>/course/<code_course>/game/<game_code>', methods=['POST'])
# def post_game_into_course(id_school, code_course, game_code):
#     return game.post_game_into_course(id_school, code_course, game_code)

# # delete an existing game from a course with game id
# @app.route('/school/<id_school>/course/<code_course>/game/<game_code>', methods=['DELETE'])
# def delete_game_from_course(id_school, code_course, game_code):
#     return game.delete_game_from_course(id_school, code_course, game_code)

# # get all games from a course with course id
# @app.route('/school/<id_school>/course/<code_course>/game', methods=['GET'])
# def get_games_from_course(id_school, code_course):
#     return game.get_games_from_course(id_school, code_course)

# # delete all games from a course with course id
# @app.route('/school/<id_school>/course/<code_course>/game', methods=['DELETE'])
# def delete_games_from_course(id_school, code_course):
#     return game.delete_games_from_course(id_school, code_course)

# SESSION ***********************************************

@app.route('/school/<id_school>/game/<game_code>/session')
def get_game_sessions(id_school, game_code):
    return session.get_game_sessions(int(id_school), game_code)
