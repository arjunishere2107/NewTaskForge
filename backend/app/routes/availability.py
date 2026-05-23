from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session as DBSession

from datetime import datetime, timedelta

from app.database import get_db

from app.models.instructor_slot import InstructorSlot

router = APIRouter()


@router.post("/generate")
def generate_slots(
    instructor_id: int,
    start_date: datetime,
    weeks: int,
    db: DBSession = Depends(get_db)
):

    created_slots = []

    current_date = start_date

    for _ in range(weeks):

        # DAILY SLOTS
        for hour in range(18, 22):

            slot_start = current_date.replace(
                hour=hour,
                minute=0,
                second=0
            )

            slot_end = slot_start + timedelta(hours=1)

            slot = InstructorSlot(
                instructor_id=instructor_id,

                start_time=slot_start,
                end_time=slot_end,

                status="available"
            )

            db.add(slot)

            created_slots.append({
                "start_time": slot_start,
                "end_time": slot_end
            })

        # NEXT WEEK
        current_date += timedelta(days=7)

    db.commit()

    return {
        "message": "Slots generated successfully",
        "total_slots": len(created_slots),
        "slots": created_slots
    }