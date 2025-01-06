from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.api.item import router as item_router
import uvicorn
import os
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from models.item import Item
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB Connection
@app.on_event("startup")
async def connect_to_mongo():
    client = AsyncIOMotorClient(os.getenv("MONGO_URI"))
    db = client[os.getenv("DB_NAME")]
    await init_beanie(database=db, document_models=[Item])

# Include routes
app.include_router(item_router, prefix="/api")


@app.get("/")
async def root():
    return {"message": "Welcome to the User Management API"}

# Run the server
if __name__ == "__main__":
    uvicorn.run("server:app", host="8.8.8.8", port=8000, reload=True)
