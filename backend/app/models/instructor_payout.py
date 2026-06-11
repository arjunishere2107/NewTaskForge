from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Date
from sqlalchemy.sql import func

from app.database import Base


class InstructorPayout(Base):
    __tablename__ = "instructor_payouts"

    id = Column(Integer, primary_key=True, index=True)

    instructor_id = Column(Integer, ForeignKey("instructors.id"))

    total_amount = Column(Float, nullable=False)

    period_start = Column(Date, nullable=False)
    period_end = Column(Date, nullable=False)

    status = Column(String, default="pending")

    processed_at = Column(DateTime(timezone=True), nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())