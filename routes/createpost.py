from fastapi import APIRouter

create_post = APIRouter()


@create_post.post("/")
def new_post():
    return {
        "message":"successfully created post"
    }

