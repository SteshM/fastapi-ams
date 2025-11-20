from fastapi import FastAPI
from app.core.database import Base, engine
from app.api.router import api_router


# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Asset Management System")


@app.get("/")
def home():
    return {"message": "Asset Management System is running"}

# Include API routes
app.include_router(api_router)
