from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from datetime import datetime

from app.database import Base


class SessionLedger(Base):
    __tablename__ = "session_ledger"

    id = Column(Integer, primary_key=True, index=True)

    enrollment_id = Column(Integer, ForeignKey("enrollments.id"))

    session_id = Column(Integer, ForeignKey("sessions.id"))

    action_type = Column(String)

    is_deducted = Column(Boolean)

    created_at = Column(DateTime, default=datetime.utcnow)