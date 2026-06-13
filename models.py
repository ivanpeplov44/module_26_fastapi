from sqlalchemy import Column, Integer, String
from database import Base


class Book(Base):
    __tablename__ = 'Book'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    call_count = Column(Integer, default=0)
