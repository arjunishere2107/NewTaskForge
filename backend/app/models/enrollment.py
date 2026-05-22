from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from app.database import Base
from datetime import datetime

class Enrollment(Base):
    __tablename__ = "enrollments"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    sessions_purchased = Column(Integer)
    
    remaining_sessions = Column(Integer)

    total_amount = Column(Float)

    status = Column(String, default="active")

    start_date = Column(DateTime)

    created_at = Column(DateTime, default=datetime.utcnow)