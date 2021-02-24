
from db import db



class UserModel(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))


    def __init__(self, username,password):
        self.username = username
        self.password = password







    @classmethod
    def find_by_name(cls, username):
        user = UserModel.query.filter_by(username=username).first()
        if user:
            return user

        return None

    @classmethod
    def find_by_id(cls,id):
        user = UserModel.query.filter_by(id=id).first()
        if user:
            return user

        return None


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


