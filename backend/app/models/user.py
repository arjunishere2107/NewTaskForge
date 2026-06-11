from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    # AUTH
    phone = Column(String, unique=True, nullable=False)

    email = Column(String, nullable=True)

    password = Column(String, nullable=False)

    # STUDENT DETAILS
    student_name = Column(String, nullable=False)

    student_age = Column(Integer, nullable=True)

    grade = Column(String, nullable=True)

    # PARENT DETAILS
    parent_name = Column(String, nullable=False)

    parent_phone = Column(String, nullable=False)

    parent_email = Column(String, nullable=True)

    # TRIAL SYSTEM
    trial_status = Column(
        String,
        default="not_started"
    )

    trial_session_id = Column(
        Integer,
        nullable=True
    )

    # ACCOUNT STATUS
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

    enrollments = relationship(
        "Enrollment",
        back_populates="user"
    )

    schedules = relationship(
        "Schedule",
        back_populates="user"
    )

    sessions = relationship(
        "Session",
        back_populates="user"
    )

    payments = relationship(
        "Payment",
        back_populates="user"
    )

    notifications = relationship(
        "Notification",
        back_populates="user"
    )