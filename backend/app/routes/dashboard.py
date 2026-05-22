from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session as DBSession

from app.database import get_db

from app.models.user import User
from app.models.instructor import Instructor
from app.models.session import Session

router = APIRouter()


@router.get("/stats")
def get_dashboard_stats(
    db: DBSession = Depends(get_db)
):

    total_students = db.query(User).count()

    total_instructors = db.query(Instructor).count()

    scheduled_sessions = (
        db.query(Session)
        .filter(Session.status == "scheduled")
        .count()
    )

    completed_sessions = (
        db.query(Session)
        .filter(Session.status == "completed")
        .count()
    )

    return {
        "total_students": total_students,
        "total_instructors": total_instructors,
        "scheduled_sessions": scheduled_sessions,
        "completed_sessions": completed_sessions
    }