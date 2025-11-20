from datetime import date
import uuid

from pydantic import BaseModel
from typing import Optional

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