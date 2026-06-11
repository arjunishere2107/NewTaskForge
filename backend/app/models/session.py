from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
    Boolean,
    Text
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class Session(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, index=True)

    # =========================
    # OWNERSHIP
    # =========================

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    enrollment_id = Column(
        Integer,
        ForeignKey("enrollments.id"),
        nullable=True
    )

    schedule_id = Column(
        Integer,
        ForeignKey("schedules.id"),
        nullable=True
    )

    # =========================
    # INSTRUCTORS
    # =========================

    # Original long-term instructor
    primary_instructor_id = Column(
        Integer,
        ForeignKey("instructors.id"),
        nullable=True
    )

    # Actual instructor who conducted class
    assigned_instructor_id = Column(
        Integer,
        ForeignKey("instructors.id"),
        nullable=True
    )

    # =========================
    # SESSION TIMING
    # =========================

    start_time = Column(
        DateTime(timezone=True),
        nullable=False
    )

    end_time = Column(
        DateTime(timezone=True),
        nullable=False
    )

    # =========================
    # CURRICULUM
    # =========================

    session_sequence_number = Column(
        Integer,
        nullable=True
    )

    module_id = Column(
    Integer,
    nullable=True
    )

    # =========================
    # TRIAL SUPPORT
    # =========================

    is_trial = Column(
        Boolean,
        default=False
    )
    is_makeup_session = Column(
        Boolean,
        default=False
    )

    # =========================
    # SESSION STATE
    # =========================

    status = Column(
        String,
        default="scheduled"
    )
    # scheduled / completed / cancelled / rescheduled / no_show

    # =========================
    # FINAL OUTCOME
    # =========================

    outcome_type = Column(
        String,
        nullable=True
    )
    # completed / no_show / technical / cancelled_late

    # =========================
    # SESSION CONSUMPTION
    # =========================

    is_deducted = Column(
        Boolean,
        default=False
    )

    # =========================
    # RESCHEDULE CHAIN
    # =========================

    rescheduled_from_session_id = Column(
        Integer,
        ForeignKey("sessions.id"),
        nullable=True
    )
    reschedule_type = Column(
        String,
        nullable=True
    )

    # =========================
    # MEETING
    # =========================

    meeting_link = Column(
        String,
        nullable=True
    )

    # =========================
    # ATTENDANCE
    # =========================

    student_join_time = Column(
        DateTime(timezone=True),
        nullable=True
    )

    teacher_join_time = Column(
        DateTime(timezone=True),
        nullable=True
    )

    # =========================
    # FEEDBACK
    # =========================

    feedback_submitted = Column(
        Boolean,
        default=False
    )

    feedback_type = Column(
        String,
        nullable=True
    )

    teacher_notes = Column(
        Text,
        nullable=True
    )

    student_feedback = Column(
        Text,
        nullable=True
    )

    # =========================
    # AUDIT
    # =========================

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    # ==================================================
    # RELATIONSHIPS
    # ==================================================

    # USER
    user = relationship(
        "User",
        back_populates="sessions"
    )

    # ENROLLMENT
    enrollment = relationship(
        "Enrollment",
        back_populates="sessions"
    )

    # SCHEDULE
    schedule = relationship(
        "Schedule",
        back_populates="sessions"
    )

    # PRIMARY INSTRUCTOR
    primary_instructor = relationship(
        "Instructor",
        foreign_keys=[primary_instructor_id],
        back_populates="primary_sessions"
    )

    # ACTUAL ASSIGNED INSTRUCTOR
    assigned_instructor = relationship(
        "Instructor",
        foreign_keys=[assigned_instructor_id],
        back_populates="assigned_sessions"
    )

    # SELF REFERENCE (RESCHEDULE)
    parent_session = relationship(
        "Session",
        remote_side=[id]
    )

    # LEDGER
    session_ledger = relationship(
        "SessionLedger",
        back_populates="session",
        uselist=False
    )

    # RESOLUTION
    resolutions = relationship(
    "SessionResolution",
    back_populates="session"
        
    )
    