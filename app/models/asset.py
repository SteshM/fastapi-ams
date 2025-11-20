# models/asset.py
from sqlalchemy import Column, String, Date, Boolean
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.core.database import Base

class Asset(Base):
    __tablename__ = "assets"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    category = Column(String, nullable=False)
    purchase_date = Column(Date, nullable=False)
    status = Column(String, nullable=False)
    deleted = Column(Boolean, default=False, nullable=False)

