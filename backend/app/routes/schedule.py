from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session as DBSession

from app.database import get_db

from app.models.schedule import Schedule

from app.schemas.schedule_schema import ScheduleCreate

router = APIRouter()


# CREATE SCHEDULE
@router.post("/")
def create_schedule(
    data: ScheduleCreate,
    db: DBSession = Depends(get_db)
):

    new_schedule = Schedule(

        user_id=data.user_id,
        enrollment_id=data.enrollment_id,

        weekday=data.weekday,

        start_time=data.start_time,
        end_time=data.end_time,

        frequency_per_week=data.frequency_per_week
    )

    db.add(new_schedule)

    db.commit()

    db.refresh(new_schedule)

    return {
        "message": "Schedule created successfully",
        "schedule_id": new_schedule.id
    }


# GET ALL SCHEDULES
@router.get("/")
def get_schedules(
    db: DBSession = Depends(get_db)
):

    schedules = db.query(Schedule).all()

    return schedules