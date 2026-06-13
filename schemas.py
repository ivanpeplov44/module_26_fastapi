from typing import Optional

from pydantic import BaseModel


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
