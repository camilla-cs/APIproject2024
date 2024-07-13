from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    content= db.Column(db.String,nullable=False)
    date = db.Column(db.Date)
    #foreign key
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    #to get info about the user
    user = db.relationship('User', back_populates='posts')

class PostSchema(ma.Schema): 
    user = fields.Nested('UserSchema', only=["id", "username", "email"])
    content = fields.String (required=True, validate=And(
        Length(min=2, error="The content of the post must be at least two characters long."),Regexp('^[A-Za-z0-9 ]+$', error="Title must have alphanumerics characters only")
        ))
    date=fields.DateTime()
                             

class Meta: 
    fields = ("id","content","date","user")
    ordered=True



post_schema= PostSchema()

posts_schema=PostSchema(many=True)

