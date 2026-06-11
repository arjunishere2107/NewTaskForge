from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    Float
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class Instructor(Base):
    __tablename__ = "instructors"

    id = Column(Integer, primary_key=True, index=True)

    # BASIC INFO
    name = Column(
        String,
        nullable=False
    )

    phone = Column(
        String,
        unique=True,
        nullable=False
    )

    email = Column(
        String,
        unique=True,
        nullable=True
    )

    # EMPLOYMENT TYPE
    type = Column(
        String,
        nullable=False
    )

    # STATUS FLAGS
    is_active = Column(
        Boolean,
        default=False
    )

    is_trained = Column(
        Boolean,
        default=False
    )

    # OPTIONAL PROFILE INFO
    expertise = Column(
        String,
        nullable=True
    )

    bio = Column(
        String,
        nullable=True
    )

    profile_image_url = Column(
        String,
        nullable=True
    )

    # WORKLOAD TRACKING
    minimum_weekly_hours = Column(
        Float,
        default=0
    )

    # SYSTEM STATE
    status = Column(
        String,
        default="active"
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

    # =========================
    # RELATIONSHIPS
    # =========================

    # SCHEDULES
    schedules = relationship(
        "Schedule",
        back_populates="instructor"
    )

    # PRIMARY INSTRUCTOR SESSIONS
    primary_sessions = relationship(
        "Session",
        foreign_keys="Session.primary_instructor_id",
        back_populates="primary_instructor"
    )

    # ASSIGNED INSTRUCTOR SESSIONS
    assigned_sessions = relationship(
        "Session",
        foreign_keys="Session.assigned_instructor_id",
        back_populates="assigned_instructor"
    )

    # AVAILABILITY
    availabilities = relationship(
        "InstructorAvailability",
        back_populates="instructor"
    )

    # SLOTS
    slots = relationship(
        "InstructorSlot",
        back_populates="instructor"
    )