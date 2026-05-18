from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db

from app.models.instructor import Instructor
from app.models.instructor_slot import InstructorSlot

from app.schemas.slot_schema import SlotCreate

router = APIRouter()


# CREATE SLOT
@router.post("/create")
def create_slot(
    slot: SlotCreate,
    db: Session = Depends(get_db)
):

    instructor = (
        db.query(Instructor)
        .filter(Instructor.id == slot.instructor_id)
        .first()
    )

    if not instructor:
        raise HTTPException(
            status_code=404,
            detail="Instructor not found"
        )

    new_slot = InstructorSlot(
        instructor_id=slot.instructor_id,
        start_time=slot.start_time,
        end_time=slot.end_time,
        status="available"
    )

    db.add(new_slot)
    db.commit()
    db.refresh(new_slot)

    return {
        "message": "Slot created successfully",
        "data": new_slot
    }


# GET ALL SLOTS
@router.get("/")
def get_slots(db: Session = Depends(get_db)):

    slots = db.query(InstructorSlot).all()

    return slots