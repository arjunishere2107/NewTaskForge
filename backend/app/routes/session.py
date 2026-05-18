from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session as DBSession

from app.database import get_db
from app.models.session import Session
from app.models.instructor_slot import InstructorSlot
from app.models.session_ledger import SessionLedger

from app.schemas.session_schema import SessionCreate

router = APIRouter()


@router.post("/create")
def create_session(
    data: SessionCreate,
    db: DBSession = Depends(get_db)
):

    # Find available instructor slot
    available_slot = (
        db.query(InstructorSlot)
        .filter(InstructorSlot.status == "available")
        .first()
    )

    if not available_slot:
        raise HTTPException(
            status_code=400,
            detail="No instructor available"
        )

    # Create session
    new_session = Session(
        user_id=data.user_id,
        enrollment_id=data.enrollment_id,

        primary_instructor_id=available_slot.instructor_id,
        assigned_instructor_id=available_slot.instructor_id,

        start_time=data.start_time,
        end_time=data.end_time,

        session_sequence_number=data.session_sequence_number,

        is_trial=data.is_trial,

        status="scheduled"
    )

    db.add(new_session)
    db.commit()
    db.refresh(new_session)

    # Mark slot as booked
    available_slot.status = "booked"
    available_slot.session_id = new_session.id

    db.commit()

    # Add ledger entry
    ledger = SessionLedger(
        enrollment_id=data.enrollment_id,
        session_id=new_session.id,
        action_type="session_booked",
        is_deducted=False
    )

    db.add(ledger)
    db.commit()

    return {
        "message": "Session created successfully",
        "session_id": new_session.id,
        "assigned_instructor": available_slot.instructor_id
    }