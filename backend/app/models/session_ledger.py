from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Float,
    DateTime
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class SessionLedger(Base):
    __tablename__ = "session_ledger"

    id = Column(Integer, primary_key=True, index=True)

    # RELATIONS
    session_id = Column(
        Integer,
        ForeignKey("sessions.id"),
        nullable=False
    )

    enrollment_id = Column(
        Integer,
        ForeignKey("enrollments.id"),
        nullable=True
    )

    instructor_id = Column(
        Integer,
        ForeignKey("instructors.id"),
        nullable=True
    )

    # SESSION FINANCIALS
    amount = Column(
        Float,
        default=0
    )

    currency = Column(
        String,
        default="INR"
    )

    ledger_type = Column(
        String,
        nullable=True
    )
    # credit / debit

    description = Column(
        String,
        nullable=True
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    # =========================
    # RELATIONSHIPS
    # =========================

    session = relationship(
        "Session",
        back_populates="session_ledger"
    )

    enrollment = relationship(
        "Enrollment",
        back_populates="session_ledgers"
    )

    instructor = relationship(
        "Instructor"
    )