from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from database import Base, engine, get_db
from models import Book
from schemas import BookCreate, BookResponse

app = FastAPI()


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get("/sync")
def hello():
    return {"message": "Hello World"}


@app.get("/book/{book_id}")
async def get_item(book_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Book).filter(Book.id == book_id))
    book = result.scalars().first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    book.call_count += 1
    await db.commit()
    return book


@app.get("/books/")
async def get_popular_books(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Book).order_by(Book.call_count.desc()))
    return result.scalars().all()


@app.post(
    "/book/",
    response_model=BookResponse,
    status_code=status.HTTP_201_CREATED)
async def create_book(book: BookCreate, db: AsyncSession = Depends(get_db)):
    db_book = Book(**book.model_dump())
    db.add(db_book)
    await db.commit()
    await db.refresh(db_book)
    return db_book
