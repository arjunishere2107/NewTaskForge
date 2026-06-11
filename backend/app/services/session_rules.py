from datetime import datetime, timedelta

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.session import Session as SessionModel


def student_weekly_session_count(
    db: Session,
    student_id: int,
    target_date: datetime,
    exclude_session_id: int = None
):
    start_of_week = target_date - timedelta(
        days=target_date.weekday()
    )

    start_of_week = start_of_week.replace(
        hour=0,
        minute=0,
        second=0,
        microsecond=0
    )

    end_of_week = start_of_week + timedelta(days=7)

    query = (
        db.query(SessionModel)
        .filter(
            SessionModel.user_id == student_id,
            SessionModel.start_time >= start_of_week,
            SessionModel.start_time < end_of_week,
            SessionModel.status.in_(
                [
                    "scheduled",
                    "live",
                    "rescheduled"
                ]
            )
        )
    )

    if exclude_session_id:
        query = query.filter(
            SessionModel.id != exclude_session_id
        )

    return query.count()


def validate_weekly_limit(
    db: Session,
    student_id: int,
    session_date: datetime,
    exclude_session_id: int = None
):
    count = student_weekly_session_count(
        db=db,
        student_id=student_id,
        target_date=session_date,
        exclude_session_id=exclude_session_id
    )

    if count >= 2:
        raise HTTPException(
            status_code=400,
            detail="Maximum 2 sessions allowed per week"
        )