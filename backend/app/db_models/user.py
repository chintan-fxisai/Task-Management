import uuid
from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
from app.db_models.base import Base
from sqlalchemy.sql import func

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    role = Column(String, nullable=False, default="employee")
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now(), server_default=func.now())
    
    def __repr__(self):
        return f"User(id={self.id}, full_name={self.full_name}, email={self.email}, role={self.role})"
