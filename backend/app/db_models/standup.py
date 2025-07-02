import uuid
from sqlalchemy import Column, ForeignKey, String,  DateTime
from sqlalchemy.dialects.postgresql import UUID
from app.db_models.base import Base
from sqlalchemy.sql import func
from enum import Enum
from sqlalchemy.types import Enum as EnumType   

class TaskCategory(Enum):
    PROJECT = "Project"
    LEARNING = "Learning"
    OTHER = "Others"

class Standup(Base):
    __tablename__ = "standups"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    user_id = Column(UUID(as_uuid=True),ForeignKey("users.id") , nullable=False)
    date = Column(DateTime(timezone=True), nullable=False)

    task_title = Column(String, nullable=False)
    task_description = Column(String, nullable=False)
    task_category = Column(EnumType(TaskCategory), nullable=False)
    
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now(), server_default=func.now())

    def __repr__(self):
        return f"Task(id={self.id}, task_title={self.task_title}, task_description={self.task_description}, task_category={self.task_category})"