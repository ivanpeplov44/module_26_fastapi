from sqlalchemy import Integer, mapped_column, String

from database import Base


class Book(Base):
    __tablename__ = "Book"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, index=True)
    description: Mapped[str] = mapped_column(String, index=True)
    call_count: Mapped[int] = mapped_column(Integer, default=0)
