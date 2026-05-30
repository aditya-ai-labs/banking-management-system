from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.transaction import router as transaction_router

from database import engine

from models import Base

from routers.customer import router as customer_router

Base.metadata.create_all(
    bind=engine
)

app = FastAPI(
    title="Banking Management System"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(
    customer_router
)

app.include_router(transaction_router)


@app.get("/")
def home():

    return {
        "message": "Banking Backend Running"
    }