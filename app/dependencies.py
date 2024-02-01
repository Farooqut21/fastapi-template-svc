from fastapi import Depends, HTTPException
from app.config import Settings

def get_settings():
    return Settings()

