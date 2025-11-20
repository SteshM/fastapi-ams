from datetime import date
import uuid

from pydantic import BaseModel
from typing import List, Optional

class AssetCreateSchema(BaseModel):
    name: str
    category: str
    purchase_date: date
    description: Optional[str] = None
    status: str


class AssetResponse(BaseModel):
    id: uuid.UUID
    name: str
    category: str
    purchase_date: date
    description: Optional[str] = None
    status: str 

    
    class Config:
        orm_mode = True

class AssetsListResponse(BaseModel):
    total: int
    items: List[AssetResponse]  


class AssetUpdateSchema(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    purchase_date: Optional[date] = None
    status: Optional[str] = None