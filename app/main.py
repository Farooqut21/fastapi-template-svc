from fastapi import FastAPI
from app.config import settings
from app.database.session import engine 
from app.database.base import Base
from app.apis.base import api_router


def create_tables():         
	Base.metadata.create_all(bind=engine)
        

def include_router(app):
    app.include_router(api_router) 

def start_application():
    app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
    create_tables()
    include_router(app)
    return app


app = start_application()


@app.get("/")
def home():
    return {"msg":"Hello FastAPI🚀"}

