from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
    Boolean
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class InstructorAvailability(Base):
    __tablename__ = "instructor_availability"

    id = Column(Integer, primary_key=True, index=True)

    instructor_id = Column(
        Integer,
        ForeignKey("instructors.id"),
        nullable=False
    )

    weekday = Column(
        String,
        nullable=False
    )

    start_time = Column(
        String,
        nullable=False
    )

    end_time = Column(
        String,
        nullable=False
    )

    is_available = Column(
        Boolean,
        default=True
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    # RELATIONSHIP
    instructor = relationship(
        "Instructor",
        back_populates="availabilities"
    )