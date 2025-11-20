from fastapi import FastAPI
from app.core.database import Base, engine


# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Asset Management System")


@app.get("/")
def home():
    return {"message": "Asset Management System is running"}
