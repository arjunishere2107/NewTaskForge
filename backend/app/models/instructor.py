from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from app.database import Base

class Instructor(Base):
    __tablename__ = "instructors"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)
    phone = Column(String)
    email = Column(String)

    type = Column(String)

    is_active = Column(Boolean, default=False)
    is_trained = Column(Boolean, default=False)

    created_at = Column(DateTime, default=datetime.utcnow)
    