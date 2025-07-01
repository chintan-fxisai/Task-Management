import uuid
from sqlalchemy import Column, String,  DateTime
from sqlalchemy.dialects.postgresql import UUID
from app.db_models.base import Base
from sqlalchemy.sql import func


class Stadup(Base):
    __tablename__ = "stadups"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    user_id = Column(UUID(as_uuid=True), nullable=False, foreign_key="users.id")
    date = Column(DateTime(timezone=True), nullable=False)
    project = Column(String, nullable=False)
    
    standup = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now(), server_default=func.now())