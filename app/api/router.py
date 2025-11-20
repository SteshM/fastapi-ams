from fastapi import APIRouter
from app.api.v1 import assets

api_router = APIRouter()
api_router.include_router(assets.router) 

