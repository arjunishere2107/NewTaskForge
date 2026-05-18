from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime

from app.database import Base


class InstructorSlot(Base):
    __tablename__ = "instructor_slots"

    id = Column(Integer, primary_key=True, index=True)

    instructor_id = Column(Integer, ForeignKey("instructors.id"))

    start_time = Column(DateTime)
    end_time = Column(DateTime)

    status = Column(String, default="available")

    session_id = Column(Integer, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)