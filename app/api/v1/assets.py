
from datetime import date
from typing import Optional
import uuid
from app.models.asset import Asset
from app.schemas.asset_schema import AssetCreateSchema, AssetResponse, AssetUpdateSchema, AssetsListResponse
from app.services.asset import create_asset, get_asset_by_id, get_assets, update_asset
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter, Query
from app.core.database import get_db

router = APIRouter(prefix="/api/v1", tags=["Assets"])

@router.post("/assets", response_model=AssetResponse)
def create_newasset(payload: AssetCreateSchema, db: Session = Depends(get_db)):
    return create_asset(db, payload)
    

@router.get("/assets/{asset_id}", response_model=AssetResponse)
def get_asset(asset_id: uuid.UUID, db: Session = Depends(get_db)):
    return get_asset_by_id(db, asset_id)

@router.get("/assets", response_model=AssetsListResponse)
def list_assets(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    name: Optional[str] = None,
    status: Optional[str] = None,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
    sort_by: Optional[str] = Query("purchase_date"),
    sort_order: Optional[str] = Query("desc"),
    db: Session = Depends(get_db)
):
    return get_assets(
        db=db,
        skip=skip,
        limit=limit,
        name=name,
        status=status,
        start_date=start_date,
        end_date=end_date,
        sort_by=sort_by,
        sort_order=sort_order
    )

@router.put("/assets/{asset_id}", response_model=AssetResponse)
def update_asset_endpoint(asset_id: uuid.UUID, data: AssetUpdateSchema, db: Session = Depends(get_db)):
    return update_asset(db, asset_id, data)