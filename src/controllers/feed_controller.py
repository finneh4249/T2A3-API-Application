"""
"""
from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.post import Post, post_schema, posts_schema

feed_controller = Blueprint('feed_controller', __name__, url_prefix='/feed')


@feed_controller.route('/', methods=['GET'])
@jwt_required()
def get_feed():
    """
    Gets a list of all posts in the database.

    Returns
    -------
    list of Post
        A list of all posts in the database.
    """
    #TODO: Add Followed Users Posts First
    # TODO: Pagination

    posts = Post.query.all().order_by(Post.created_at.desc())

    post_arr = posts_schema.jsonify(posts)
    return post_arr

@feed_controller.route('/following', methods=['GET'])
@jwt_required()
def get_following_feed():
    """
    Gets a list of all posts from users the current user is following.

    Returns
    -------
    list of Post
        A list of all posts from followed users.
    """
    pass
