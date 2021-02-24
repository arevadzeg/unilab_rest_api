
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.iphones import IphoneModel


from models.user import UserModel



class Iphones(Resource):


    def get(self, name):
        phone = IphoneModel.find_by_name(name)
        user_objects = UserModel.query.all()

        for item in user_objects:
            print(item.id)
            # users.append(UserModel(item.id, item.username, item.password))


        if phone:
            return phone
        return 'No such phone'


    @jwt_required()
    def put(self, name):
        my_parser = reqparse.RequestParser()


        my_parser.add_argument(
            'quantity',
            required=True
        )
        my_parser.add_argument(
            'price',
            required=True
        )
        item = IphoneModel.find_by_name(name)

        if item:

            parsed = my_parser.parse_args()


            item.price = parsed['price']
            item.quantity = parsed['quantity']
            item.save_to_db()
            return {'message': "Succsess"}, 400



        return {"Message": "We do not have such Phone"},404


        # parsed = my_parser.parse_args()
        # return IphoneModel.update_details(name,parsed['price'],parsed['quantity'])


    @jwt_required()
    def post(self, name):

        my_parser = reqparse.RequestParser()


        my_parser.add_argument(
            'quantity',
            required=True
        )
        my_parser.add_argument(
            'price',
            required=True
        )

        if IphoneModel.find_by_name(name):
            return {'message': "Iphone already in database"}

        parsed = my_parser.parse_args()

        phone = IphoneModel(name,parsed['quantity'],parsed['price'])
        print(phone)

        phone.save_to_db()
        return {"Message" :"Succsess"}




    @jwt_required()
    def delete(self,name):
        phone = IphoneModel.find_by_name(name)
        if phone:
            phone.delete_from_db()
            return {"Message" :"Succsess"}
        return {"Message" :"No such Phone"}


#
# class AllIphones(Resource):
#
#     def get(self):
#         print(all_users)
#         return  all_users
#
