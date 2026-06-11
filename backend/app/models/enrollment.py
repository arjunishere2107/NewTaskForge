from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class Enrollment(Base):
    __tablename__ = "enrollments"

    id = Column(Integer, primary_key=True, index=True)

    # USER LINK
    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    # PURCHASE INFO
    sessions_purchased = Column(
        Integer,
        nullable=False
    )

    # PRICING
    total_amount = Column(
        Float,
        nullable=False
    )

    discount_amount = Column(
        Float,
        default=0
    )

    final_amount_paid = Column(
        Float,
        nullable=False
    )

    # OPTIONAL PAYMENT LINK
    payment_id = Column(
        Integer,
        ForeignKey("payments.id"),
        nullable=True
    )

    # LIFECYCLE
    start_date = Column(
        DateTime(timezone=True),
        nullable=True
    )

    end_date = Column(
        DateTime(timezone=True),
        nullable=True
    )

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

    # RELATIONSHIPS

    user = relationship(
        "User",
        back_populates="enrollments"
    )

    schedules = relationship(
        "Schedule",
        back_populates="enrollment"
    )

    sessions = relationship(
        "Session",
        back_populates="enrollment"
    )

    session_ledgers = relationship(
        "SessionLedger",
        back_populates="enrollment"
    )

    payments = relationship(
        "Payment",
        back_populates="enrollment",
        foreign_keys="Payment.enrollment_id"
    )