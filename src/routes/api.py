from flask import request
from main import app
from src.controllers.api.v1.post_controller import PostController as PostApiControllerV1
from src.entities.post import Post
from src.helpers.adapters.request_entity.post.collection.posts_adapter import PostsAdapter
from src.helpers.adapters.request_entity.post.post_adapter import PostAdapter
from src.repositories.post_repository import PostRepository
from src.services.crud.post_service import PostService

# API VERSION #1
# POSTS
post_adapter = PostAdapter()
post_api_controller_v1 = PostApiControllerV1(
    PostService(
        PostRepository(Post())
    ),
    post_adapter
    ,
    PostsAdapter(post_adapter)
)


@app.route("/api/v1/posts/all", methods=['GET'])
def posts_all_v1():
    return post_api_controller_v1.get_all()


@app.route("/api/v1/posts/get", methods=['GET'])
def post_get_v1():
    return post_api_controller_v1.get(request)
