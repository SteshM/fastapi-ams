import uuid
from app.schemas.asset_schema import AssetCreateSchema
from sqlalchemy.orm import Session
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

def get_asset_by_id(db: Session, asset_id: uuid.UUID) -> Asset:
    asset = db.query(Asset).filter(Asset.id == asset_id).first()
    if not asset:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Asset with id {asset_id} not found"
        )
    return asset
