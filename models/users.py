from pydantic import BaseModel, EmailStr
from typing import List
from models.events import Event


class User(BaseModel):
    email: EmailStr
    password: str
    events: List[Event] | None
    

    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@gmail.com",
                "password": "strong!!!passw",
                "events": [],
                }
            }
    
    
class UserSignIn(BaseModel):
    email: EmailStr
    password: str
    
    class Config:
        schema_extra = {
            "example": {
                "email": fastapi@packt.com,
                "password": "strong!!!",
                }
            }
    
    
    