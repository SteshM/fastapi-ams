from datetime import date
from pydantic import BaseModel
from typing import Optional

class AssetSchema(BaseModel):
    name: str
    category: str
    purchase_date: date

    class AssetResponse(BaseModel): 
        id: str
        name: str
        category: str
        purchase_date: date
        description: Optional[str] = None
        status: str


    class Config:
        orm_mode = True