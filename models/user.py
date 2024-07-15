from init import db, ma 
from marshmallow import fields
from marshmallow.validate import Regexp, Range

from models.event import Event,event_schema,events_schema
from models.event_user import EventUser

class User(db.Model): 
    __tablename__="users"
    id = db.Column(db.Integer, primary_key=True) 
    username = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True) 
    experience_level= db.Column(db.Integer, nullable=False)
    bio = db.Column(db.String, nullable=True)
    password = db.Column (db.String,nullable=False)
    is_admin= db.Column (db.Boolean,default=False) 

    #to connect to post model 
    posts = db.relationship('Post', back_populates="user")
    #to connect to event model 
    events=db.relationship("Event",secondary="event_user",backref="users",cascade="all,delete")




class UserSchema (ma.Schema): 
    username = fields.String(required=True) 
    email = fields.String(required=True, validate=Regexp("", error="Invalid Email Format. ")) 
    bio = fields.String(allow_none=True)
    password = fields.String(required=True, validate=Regexp("^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", error="Minimum eight characters, at least one letter and one number. "))
    experience_level = fields.Integer(required=True, validate=Range(min=0, max=17, error="Please choose a number from 0 to 17."))
    posts=fields.List(fields.Nested('PostSchema'),exclude=["user"])
   
    class Meta: 
        fields = ("id", "username", "email", "experience_level", "bio", "password", "is_admin","posts")
        ordered = True 

user_schema = UserSchema(exclude=["password"])
users_schema = UserSchema(many=True, exclude=["password"]) 

