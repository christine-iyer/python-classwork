from sqlalchemy.orm import Session
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite Database URL
DATABASE_URL = "sqlite:///./test.db"

# Create SQLite engine and session
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Create tables
Base.metadata.create_all(bind=engine)

def create_user(db: Session, first_name: str):
    db_user = User(first_name=first_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    return db.query(User).all()
