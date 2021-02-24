from flask_restful import Resource, reqparse
from models.user import UserModel
from flask_jwt import jwt_required





class Register(Resource):

    my_parser = reqparse.RequestParser()

    my_parser.add_argument(
        'username',
        required=True
    )
    my_parser.add_argument(
        'password',
        required=True
    )

    def post(self):
        params = Register.my_parser.parse_args()

        if UserModel.find_by_name(params['username']):
            return {'Message': 'Such user already exists'}

        new_user = UserModel(params['username'], params['password'])
        new_user.save_to_db()

        return {"Message": "Success"}


class Users(Resource):

    @jwt_required()
    def post(self, id):
        user = UserModel.find_by_id(id)
        return user
#