from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.api.user import router as user_router
import uvicorn
import os
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

# Include routes
app.include_router(user_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Welcome to the User Management API"}

# Run the server
if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)


