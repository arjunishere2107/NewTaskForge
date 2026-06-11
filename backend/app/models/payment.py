from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
    Float
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)

    # RELATIONS
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

    # PAYMENT INFO
    amount = Column(
        Float,
        nullable=False
    )

    payment_mode = Column(
        String,
        nullable=False
    )
    # razorpay / upi / cash / bank_transfer

    transaction_reference = Column(
        String,
        nullable=True
    )

    gateway_payment_id = Column(
        String,
        nullable=True
    )

    gateway_order_id = Column(
        String,
        nullable=True
    )

    # STATUS
    status = Column(
        String,
        default="pending"
    )
    # pending / success / failed / refunded

    # REFUND SUPPORT
    refund_amount = Column(
        Float,
        default=0
    )

    refund_reason = Column(
        String,
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
        back_populates="payments"
    )

    enrollment = relationship(
        "Enrollment",
        back_populates="payments",
        foreign_keys=[enrollment_id]
    )