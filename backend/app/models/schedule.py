from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from app.database import Base


class Schedule(Base):
    __tablename__ = "schedules"

    id = Column(Integer, primary_key=True, index=True)

    # RELATIONS
    user_id = Column(Integer, ForeignKey("users.id"))
    enrollment_id = Column(Integer, ForeignKey("enrollments.id"))

    primary_instructor_id = Column(
        Integer,
        ForeignKey("instructors.id")
    )

    # RECURRING PATTERN
    weekday = Column(String)
    start_time = Column(DateTime)
    end_time = Column(DateTime)

    # WEEKLY FREQUENCY
    frequency_per_week = Column(Integer, default=1)

    # STATUS
    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime)