from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    phone = Column(String, unique=True)
    email = Column(String, nullable=True)
    password = Column(String)

    student_name = Column(String)
    student_age = Column(Integer)

    parent_name = Column(String)
    parent_phone = Column(String)

    trial_status = Column(String, default="not_started")

    status = Column(String, default="active")

    created_at = Column(DateTime, default=datetime.utcnow)