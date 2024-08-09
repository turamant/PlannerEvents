from pydantic import BaseModel
from typing import List


class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str
    tags: List[str]
    location: str
    
    
class Config:
    schema_extra = {
        "example": {
            "title": "Первый рабочий день - я web backend разработчик",
            "image": "https://linktomyimage.com/image.png",
            "description":"Обсуждение: самый первый день на новой работе",
            "tags": ["обсуждение", "web", "backend", "разработчик"],
            "location": "telegram chanel"
        }
    }
    