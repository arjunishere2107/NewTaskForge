from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    Time,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class Schedule(Base):
    __tablename__ = "schedules"

    id = Column(Integer, primary_key=True, index=True)

    # OWNERSHIP
    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    enrollment_id = Column(
        Integer,
        ForeignKey("enrollments.id"),
        nullable=False
    )

    # INSTRUCTOR RELATIONSHIP
    primary_instructor_id = Column(
        Integer,
        ForeignKey("instructors.id"),
        nullable=False
    )

    # RECURRING PATTERN
    day_of_week = Column(
        String,
        nullable=False
    )

    slot_start_time = Column(
        Time,
        nullable=False
    )

    slot_end_time = Column(
        Time,
        nullable=False
    )

    # WEEKLY FREQUENCY
    sessions_per_week = Column(
        Integer,
        default=1
    )

    # LIFECYCLE
    start_date = Column(
        Date,
        nullable=False
    )

    end_date = Column(
        Date,
        nullable=True
    )

    # STATE
    status = Column(
        String,
        default="active"
    )
    # active / paused / ended / replaced

    # VERSIONING
    replaced_by_schedule_id = Column(
        Integer,
        ForeignKey("schedules.id"),
        nullable=True
    )

    # AUDIT
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    # RELATIONSHIPS

    user = relationship(
        "User",
        back_populates="schedules"
    )

    enrollment = relationship(
        "Enrollment",
        back_populates="schedules"
    )

    sessions = relationship(
        "Session",
        back_populates="schedule"
    )

    instructor = relationship(
        "Instructor",
        back_populates="schedules"
    )