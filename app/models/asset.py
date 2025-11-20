import uuid
from sqlalchemy import Column, String, Date
from app.core.database import Base
class Asset(Base):
    __tablename__ = "assets"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, index=True)
    description = Column(String, index=True)
    category = Column(String)
    purchase_date = Column(Date)
    status = Column(String, default="available")
