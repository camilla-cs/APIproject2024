from init import db, ma
from marshmallow import fields, validates
from marshmallow.validate import Length, And, Regexp, OneOf
from marshmallow.exceptions import ValidationError

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    content= db.Column(db.String)
    date = db.Column(db.Date)
    #foreign key
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    #to get info about the user
    user = db.relationship('User', back_populates='posts')

class PostSchema(ma.Schema): 
    user = fields.Nested('UserSchema', only=["id", "name", "email"])
    content = fields.String (required=True, validate=And(
        Length(min=2, error="The content of the post must be at least two characters long."),Regexp('^[A-Za-z0-9 ]+$', error="Title must have alphanumerics characters only")
        ))
                             

class Meta: 
    fields = ("id","content","date","user")
    ordered=True

#to handle a single post object
post_schema= PostSchema()
#to handle a list of post objects 
posts_schema=PostSchema(many=True)

