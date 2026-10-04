from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column

engine = create_engine(url='sqlite:///requests.db')

session = sessionmaker(engine)

class Base(DeclarativeBase):
    pass

class ChatRequests(Base):
    __tablename__ = "chat_requests"

    id: Mapped[int] = mapped_column(primary_key=True)
    ip_adrr: Mapped[str] = mapped_column(index=True)
    promt: Mapped[str]
    response: Mapped[str]