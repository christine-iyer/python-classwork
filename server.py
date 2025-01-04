from fastapi import FastAPI
from routes.api.user import router as user_router
import uvicorn
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from models.user import User

# SQLite Database URL
DATABASE_URL = "sqlite:///./test.db"

# Create SQLite engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define the base
Base = declarative_base()

# Debugging: Print before creating tables
print("Creating tables...")

# Create tables
Base.metadata.create_all(bind=engine)  # <--- THIS LINE CREATES TABLES

print("Tables created!")

# Initialize FastAPI app
app = FastAPI()

# Include routes
app.include_router(user_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "SQLite FastAPI Server is running!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
