
from http.client import HTTPException
import uuid
from app.models.asset import Asset
from app.schemas.asset_schema import AssetCreateSchema, AssetResponse
from app.services.asset import create_asset, get_asset_by_id
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter
from app.core.database import get_db

router = APIRouter(prefix="/api/v1", tags=["Assets"])

@router.post("/assets", response_model=AssetResponse)
def create_newasset(payload: AssetCreateSchema, db: Session = Depends(get_db)):
    return create_asset(db, payload)
    


@router.get("/assets/{asset_id}", response_model=AssetResponse)
def get_asset(asset_id: uuid.UUID, db: Session = Depends(get_db)):
    return get_asset_by_id(db, asset_id)