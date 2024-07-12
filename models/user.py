from init import db, ma 
from marshmallow import fields
from marshmallow.validate import Regexp  

class User(db.Model): 
    __tablename__="users"
    id = db.Column(db.Integer, primary_key=True) 
    username = db.Column(db.String) 
    email = db.Column(db.String, nullable=False, unique=True) 
    experience_level= db.Column(db.Integer, nullable=False)
    bio = db.Column(db.String, nullable=True)
    password = db.Column (db.String,nullable=False)
    is_admin= db.Column (db.Boolean,default=False) 


class UserSchema (ma.Schema): 
    email = fields.String(required=True, validate=Regexp("", error="Invalid Email Format. ")) 

    password = fields.String(required=True, validate=Regexp("^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", error="Minimum eight characters, at least one letter and one number. "))
    experience_level = fields.String(required=True, validate=Regexp("", error="Please choose a number from 0 to 17. "))

    class Meta: 
        fields = ("id", "username", "email", "password", "is_admin")

user_schema = UserSchema(exclude=["password"])
users_schema = UserSchema(many=True, exclude=["password"]) 

