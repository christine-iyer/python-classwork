from models.user import User

# In-memory "database"
users = []

async def create_user(user: User):
    users.append(user)
    return user

async def get_users():
    return users
