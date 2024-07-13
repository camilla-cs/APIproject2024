from datetime import date

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.post import Post, PostSchema, post_schema, posts_schema
from models.user import User

posts_bp = Blueprint("posts", __name__, url_prefix="/posts")


#to get all the posts
@posts_bp.route("/", methods=["GET"])
def get_all_posts():
    stmt = db.select(Post).order_by(Post.date.desc())
    posts = db.session.scalars(stmt).all()
    return posts_schema.dump(posts),200 

#to get one post
@posts_bp.route("/<int:id>")
def get_one_post(id): 
    stmt = db.select(Post).filter_by(id=id)
    post = db.session.scalar(stmt)
    if post: 
        return post_schema.dump(post)
    else:
        return {"error":f"Post with id {id} not found. "}, 404
    
#to create new post
@posts_bp.route("/", methods=["POST"])
@jwt_required()
def create_post():
    body_data = request.get_json()
    post = Post (
        content= body_data.get("content"),
        date=date.today(),
        user_id=get_jwt_identity()
    )

    db.session.add(post)
    db.session.commit()

    return post_schema.dump(post)

#to delete a post 
@posts_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_post(id): 
    stmt = db.select(Post).filter_by(id=id)
    post = db.session.scalar(stmt)

    if post: 
        db.session.delete(post)
        db.session.commit()
        return {"message": f"Post '{id}' deleted successfully"}
    else:
        return {"error": f"Post with id {id} not found"}, 404 
    
#to edit a post
@posts_bp.route("/<int:id>", methods=["PUT","PATCH"])
@jwt_required()
def edit_post(id): 
    body_data = request.get_json()
    stmt = db.select(Post).filter_by(id=id)
    post = db.session.scalar(stmt)

    if post:
        post.content = body_data.get("content") or post.content

        db.session.commit()
        return post_schema.dump(post)
    
    else:
        return {"error":f"Post with id {id} not found. "}, 404
    
