from fastapi import APIRouter

from api.routes import books, telex_integration

api_router = APIRouter()
api_router.include_router(books.router, prefix="/books", tags=["books"])
api_router.include_router(telex_integration.router, prefix="/test", tags=["telex"])
