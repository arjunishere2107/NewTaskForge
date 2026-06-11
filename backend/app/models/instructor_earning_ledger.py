from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime
from sqlalchemy.sql import func

from app.database import Base


class InstructorEarningLedger(Base):
    __tablename__ = "instructor_earning_ledger"

    id = Column(Integer, primary_key=True, index=True)

    instructor_id = Column(Integer, ForeignKey("instructors.id"))

    session_id = Column(Integer, ForeignKey("sessions.id"), nullable=True)

    event_type = Column(String, nullable=False)

    amount = Column(Float, nullable=False)

    reference_id = Column(Integer, nullable=True)

    is_paid = Column(Boolean, default=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())