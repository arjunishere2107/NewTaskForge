from sqlalchemy import Column, Integer, String, DateTime, JSON
from sqlalchemy.sql import func

from app.database import Base


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)

    entity_type = Column(String, nullable=False)
    entity_id = Column(Integer, nullable=False)

    action_type = Column(String, nullable=False)

    old_value = Column(JSON, nullable=True)
    new_value = Column(JSON, nullable=True)

    performed_by = Column(String, nullable=False)
    performed_by_id = Column(Integer, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())