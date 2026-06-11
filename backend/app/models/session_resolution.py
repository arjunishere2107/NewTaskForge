from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
    DateTime,
    Text
)

from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database import Base


class SessionResolution(Base):
    __tablename__ = "session_resolutions"

    id = Column(Integer, primary_key=True, index=True)

    session_id = Column(
        Integer,
        ForeignKey("sessions.id"),
        nullable=False
    )

    final_outcome_type = Column(
        String,
        nullable=False
    )

    resolved_by = Column(
        String,
        nullable=False
    )

    resolution_source = Column(
        String,
        nullable=False
    )

    resolved_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    has_conflict = Column(
        Boolean,
        default=False
    )

    conflict_reason = Column(
        Text,
        nullable=True
    )

    admin_notes = Column(
        Text,
        nullable=True
    )

    is_finalized = Column(
        Boolean,
        default=False
    )

    # RELATIONSHIP
    session = relationship(
        "Session",
        back_populates="resolutions"
    )