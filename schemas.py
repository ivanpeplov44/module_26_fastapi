from pydantic import BaseModel
from typing import Optional


class BookCreate(BaseModel):
    title: str
    description: Optional[str] = None

class BookResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    call_count: int

    class Config:
        from_attributes = True
