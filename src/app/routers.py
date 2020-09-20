from fastapi import APIRouter
from src.app.user.api import user_router
# from src.app.blog.api import blog_router

api_router = APIRouter()

# api_router.include_router(blog_router, prefix="/blog", tags=["blog"])
api_router.include_router(user_router, prefix='/user', tags=["user"])
