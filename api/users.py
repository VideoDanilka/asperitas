from flask import jsonify
from flask_restful import Resource, reqparse, abort

from app.app2 import main_app

from tools.misc import create_jwt_for_user

parser = reqparse.RequestParser()
parser.add_argument('username')
parser.add_argument('password')


class RegisterRes(Resource):
    def post(self):
        args = parser.parse_args()
        created_user = main_app.user_repo.request_create(args['username'], args['password'])
        if created_user is None:
            abort(400, message='Duplicated username')
        return create_jwt_for_user(created_user)


class LoginRes(Resource):
    def post(self):
        args = parser.parse_args()
        user, error = main_app.user_repo.authorize(args['username'], args['password'])
        if user is None:
            abort(400, message=error)
        return create_jwt_for_user(user)


class UserPost(Resource):
    def get(self, user_login):
        return jsonify(main_app.post_repo.get_by_username(user_login))
