from beanie import Document
from pydantic import Field

class Item(Document):
    name: str = Field(...)
    quantity: int = Field(...)
    cost: float = Field(...)
    
    class Settings:
        collection = "items"
    

    
    
    