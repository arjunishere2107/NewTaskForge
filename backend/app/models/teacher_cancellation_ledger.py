from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.sql import func

from app.database import Base


class TeacherCancellationLedger(Base):
    __tablename__ = "teacher_cancellation_ledger"

    id = Column(Integer, primary_key=True, index=True)

    instructor_id = Column(Integer, ForeignKey("instructors.id"))

    session_id = Column(Integer, ForeignKey("sessions.id"))

    cancellation_type = Column(String, nullable=False)

    penalty_applied = Column(Boolean, default=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())