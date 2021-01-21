from src.extensions.database import db
from src.extensions.marshmallow import ma


class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80))

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email


class userSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = user


user_schema = userSchema()
users_schema = userSchema(many=True)
