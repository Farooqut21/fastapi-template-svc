from fastapi import APIRouter

from app.apis.v1 import route_org

api_router = APIRouter()
api_router.include_router(route_org.router, prefix="", tags=["organizations"])
