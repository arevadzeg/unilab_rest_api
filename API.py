from flask import Flask, redirect
from flask_jwt import  JWT
from security import authentication, identity
from resources.iphones import Iphones
# from resources.iphones import AllIphones

from flask_restful import Api

from resources.user import Users, Register





app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base.db'
api = Api(app)
jwt = JWT(app, authentication, identity)
app.config['PROPAGATE_EXCEPTIONS'] = True


@app.route("/")
def home():
    return redirect('https://github.com/arevadzeg/unilab_rest_api/tree/main'), 302

@app.before_first_request
def create_table():
    db.create_all()




# api.add_resource(AllIphones,'/Iphones')


api.add_resource(Iphones,'/Iphones/<string:name>')



api.add_resource(Register,'/Register')

api.add_resource(Users,'/User/<string:id>')



if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True)