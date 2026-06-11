from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base


class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)

    # IMPORTANT FIX
    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    user_type = Column(String, nullable=False)

    type = Column(String, nullable=False)

    title = Column(String, nullable=False)

    message = Column(String, nullable=False)

    status = Column(
        String,
        default="sent"
    )

    sent_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    # RELATIONSHIP
    user = relationship(
        "User",
        back_populates="notifications"
    )