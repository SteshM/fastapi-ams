from datetime import date
from typing import Optional
import uuid
from app.schemas.asset_schema import AssetCreateSchema, AssetUpdateSchema
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.asset import Asset
from fastapi import HTTPException, status


def create_asset(db: Session, data: AssetCreateSchema):
    try:
        asset = Asset(
            name=data.name,
            description=data.description,
            category=data.category,
            purchase_date=data.purchase_date,
            status=data.status
        )
        db.add(asset)
        db.commit()
        db.refresh(asset)   # <-- refresh so ORM object has id
        return asset        # <-- return SQLAlchemy object
    except Exception as e:
        db.rollback()
        raise e



def get_asset_by_id(db: Session, asset_id: uuid.UUID, include_deleted: bool = False):
    query = db.query(Asset).filter(Asset.id == asset_id)
    if not include_deleted:
        query = query.filter(Asset.deleted == False)
    return query.first()


def get_assets(
    db: Session,
    skip: int = 0,
    limit: int = 10,
    name: Optional[str] = None,
    status: Optional[str] = None,
    deleted: Optional[bool] = False,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
    sort_by: str = "purchase_date",
    sort_order: str = "desc"
) -> dict:

    query = db.query(Asset)

    # Filters
    if name:
        query = query.filter(Asset.name.ilike(f"%{name}%"))
    if status:
        query = query.filter(Asset.status == status)

    if deleted is False:
        query = query.filter(Asset.deleted == False)
    elif deleted is True:
        query = query.filter(Asset.deleted == True) 



    if start_date:
        query = query.filter(Asset.purchase_date >= start_date)
    if end_date:
        query = query.filter(Asset.purchase_date <= end_date)

    # Total count before pagination
    total = query.with_entities(func.count()).scalar()

    # Sorting
    if sort_by in {"name", "purchase_date", "status", "category"}:
        column = getattr(Asset, sort_by)
        if sort_order.lower() == "desc":
            column = column.desc()
        else:
            column = column.asc()
        query = query.order_by(column)

    # Pagination
    items = query.offset(skip).limit(limit).all()

    return {"total": total, "items": items}




def update_asset(db: Session, asset_id: uuid.UUID, data: AssetUpdateSchema):
    asset = db.query(Asset).filter(Asset.id == asset_id).first()
    if not asset:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Asset with id {asset_id} not found"
        )
    
    # Update only provided fields
    for field, value in data.dict(exclude_unset=True).items():
        setattr(asset, field, value)
    
    db.commit()
    db.refresh(asset)
    return asset




def soft_delete_asset(db: Session, asset_id: uuid.UUID):
    asset = db.query(Asset).filter(Asset.id == asset_id, Asset.deleted == False).first()
    if not asset:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Asset with id {asset_id} not found or already deleted"
        )
    
    asset.deleted = True
    db.commit()
    return {"message": f"Asset {asset_id} successfully soft-deleted"}


