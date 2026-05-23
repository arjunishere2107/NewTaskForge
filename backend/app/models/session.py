from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Text
from app.database import Base
from datetime import datetime

class Session(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    enrollment_id = Column(Integer, ForeignKey("enrollments.id"))

    primary_instructor_id = Column(Integer)
    assigned_instructor_id = Column(Integer)

    start_time = Column(DateTime)
    end_time = Column(DateTime)

    session_sequence_number = Column(Integer)

    is_trial = Column(Boolean, default=False)

    status = Column(String, default="scheduled")

    outcome_type = Column(String, nullable=True)

    is_deducted = Column(Boolean, default=False)

    rescheduled_from_session_id = Column(Integer, nullable=True)

    student_join_time = Column(DateTime, nullable=True)
    teacher_join_time = Column(DateTime, nullable=True)

    feedback_submitted = Column(Boolean, default=False)

    created_at = Column(DateTime, default=datetime.utcnow)
    
    teacher_notes = Column(Text, nullable=True)
    student_feedback = Column(Text, nullable=True)