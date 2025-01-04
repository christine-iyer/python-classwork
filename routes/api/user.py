from fastapi import APIRouter 
from models.user import User
from controllers.api.user import create_user, get_users

router = APIRouter()

@router.post("/user")
async def add_user(user:User):
     return await create_user(user)

@router.get("/users")
async def list_users():
     return await get_users()

