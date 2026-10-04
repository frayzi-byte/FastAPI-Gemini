from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from requests_router import router
from contextlib import asynccontextmanager
from db import Base, engine

@asynccontextmanager
async def lifespan(app : FastAPI):
    Base.metadata.create_all(engine)
    print("TABLES CREATED")
    yield

app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500", "http://127.0.0.1:5500"],
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)
app.include_router(router)

#test