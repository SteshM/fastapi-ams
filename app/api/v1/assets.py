
from app.schemas.asset_schema import AssetCreateSchema, AssetResponse
from app.services.asset import create_asset
from sqlalchemy.orm import Session
from fastapi import Depends
from app.core.database import get_db
from fastapi import APIRouter

router = APIRouter(prefix="/api/v1", tags=["Assets"])

@router.post("/assets", response_model=AssetResponse)
def create_newasset(payload: AssetCreateSchema, db: Session = Depends(get_db)):
    return create_asset(db, payload)
    
