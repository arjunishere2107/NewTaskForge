from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session as DBSession
from datetime import datetime

from app.database import get_db

from app.models.session import Session
from app.models.instructor_slot import InstructorSlot
from app.models.session_ledger import SessionLedger
from app.models.enrollment import Enrollment

from app.schemas.session_schema import SessionCreate

router = APIRouter()


# CREATE SESSION
@router.post("/")
def create_session(
    data: SessionCreate,
    db: DBSession = Depends(get_db)
):

    # CHECK AVAILABLE SLOT
    available_slot = (
        db.query(InstructorSlot)
        .filter(
            InstructorSlot.status == "available",
            InstructorSlot.start_time == data.start_time,
            InstructorSlot.end_time == data.end_time
        )
        .first()
    )

    # IF NO SLOT FOUND
    if not available_slot:
        raise HTTPException(
            status_code=404,
            detail="No instructor slot available"
        )

    # CREATE SESSION
    new_session = Session(
        user_id=data.user_id,
        enrollment_id=data.enrollment_id,

        primary_instructor_id=available_slot.instructor_id,
        assigned_instructor_id=available_slot.instructor_id,

        start_time=data.start_time,
        end_time=data.end_time,

        session_sequence_number=data.session_sequence_number,

        is_trial=data.is_trial,

        status="scheduled",

        is_deducted=False
    )

    db.add(new_session)
    db.commit()
    db.refresh(new_session)

    # UPDATE SLOT STATUS
    available_slot.status = "booked"
    available_slot.session_id = new_session.id

    db.commit()

    return {
        "message": "Session created successfully",
        "session_id": new_session.id,
        "assigned_instructor_id": available_slot.instructor_id
    }


# COMPLETE SESSION
@router.put("/complete/{session_id}")
def complete_session(
    session_id: int,
    db: DBSession = Depends(get_db)
):

    session = (
        db.query(Session)
        .filter(Session.id == session_id)
        .first()
    )

    if not session:
        raise HTTPException(
            status_code=404,
            detail="Session not found"
        )

    # PREVENT DOUBLE DEDUCTION
    if session.is_deducted:
        raise HTTPException(
            status_code=400,
            detail="Session already deducted"
        )

    # UPDATE SESSION
    session.status = "completed"
    session.is_deducted = True

    # UPDATE ENROLLMENT
    enrollment = (
        db.query(Enrollment)
        .filter(Enrollment.id == session.enrollment_id)
        .first()
    )

    if enrollment and enrollment.remaining_sessions > 0:
        enrollment.remaining_sessions -= 1

    # CREATE LEDGER ENTRY
    ledger = SessionLedger(
        enrollment_id=session.enrollment_id,
        session_id=session.id,
        action_type="session_completed",
        is_deducted=True
    )

    db.add(ledger)

    db.commit()

    return {
        "message": "Session completed successfully"
    }


# RESCHEDULE SESSION
@router.put("/reschedule/{session_id}")
def reschedule_session(
    session_id: int,
    new_start_time: datetime,
    new_end_time: datetime,
    db: DBSession = Depends(get_db)
):

    session = (
        db.query(Session)
        .filter(Session.id == session_id)
        .first()
    )

    if not session:
        raise HTTPException(
            status_code=404,
            detail="Session not found"
        )

    # FIND NEW AVAILABLE SLOT
    available_slot = (
        db.query(InstructorSlot)
        .filter(
            InstructorSlot.status == "available",
            InstructorSlot.start_time == new_start_time,
            InstructorSlot.end_time == new_end_time
        )
        .first()
    )

    if not available_slot:
        raise HTTPException(
            status_code=404,
            detail="No slot available for reschedule"
        )

    # FREE OLD SLOT
    old_slot = (
        db.query(InstructorSlot)
        .filter(InstructorSlot.session_id == session.id)
        .first()
    )

    if old_slot:
        old_slot.status = "available"
        old_slot.session_id = None

    # ASSIGN NEW SLOT
    available_slot.status = "booked"
    available_slot.session_id = session.id

    # UPDATE SESSION
    session.start_time = new_start_time
    session.end_time = new_end_time
    session.assigned_instructor_id = available_slot.instructor_id

    db.commit()

    return {
        "message": "Session rescheduled successfully"
    }


# STUDENT JOIN
@router.put("/student-join/{session_id}")
def student_join(
    session_id: int,
    db: DBSession = Depends(get_db)
):

    session = (
        db.query(Session)
        .filter(Session.id == session_id)
        .first()
    )

    if not session:
        raise HTTPException(
            status_code=404,
            detail="Session not found"
        )

    session.student_join_time = datetime.utcnow()

    db.commit()

    return {
        "message": "Student joined successfully",
        "join_time": session.student_join_time
    }


# TEACHER JOIN
@router.put("/teacher-join/{session_id}")
def teacher_join(
    session_id: int,
    db: DBSession = Depends(get_db)
):

    session = (
        db.query(Session)
        .filter(Session.id == session_id)
        .first()
    )

    if not session:
        raise HTTPException(
            status_code=404,
            detail="Session not found"
        )

    session.teacher_join_time = datetime.utcnow()

    db.commit()

    return {
        "message": "Teacher joined successfully",
        "join_time": session.teacher_join_time
    }


# CANCEL SESSION
@router.put("/cancel/{session_id}")
def cancel_session(
    session_id: int,
    db: DBSession = Depends(get_db)
):

    session = (
        db.query(Session)
        .filter(Session.id == session_id)
        .first()
    )

    if not session:
        raise HTTPException(
            status_code=404,
            detail="Session not found"
        )

    # CANCEL SESSION
    session.status = "cancelled"

    # FREE SLOT AGAIN
    slot = (
        db.query(InstructorSlot)
        .filter(InstructorSlot.session_id == session.id)
        .first()
    )

    if slot:
        slot.status = "available"
        slot.session_id = None

    db.commit()

    return {
        "message": "Session cancelled successfully"
    }


# GET ALL SESSIONS
@router.get("/")
def get_sessions(
    db: DBSession = Depends(get_db)
):

    sessions = db.query(Session).all()

    return sessions


# GET USER SESSIONS
@router.get("/user/{user_id}")
def get_user_sessions(
    user_id: int,
    status: str = None,
    db: DBSession = Depends(get_db)
):

    query = (
        db.query(Session)
        .filter(Session.user_id == user_id)
    )

    # FILTER BY STATUS
    if status:
        query = query.filter(Session.status == status)

    sessions = query.all()

    return sessions


# GET SINGLE SESSION
@router.get("/{session_id}")
def get_single_session(
    session_id: int,
    db: DBSession = Depends(get_db)
):

    session = (
        db.query(Session)
        .filter(Session.id == session_id)
        .first()
    )

    if not session:
        raise HTTPException(
            status_code=404,
            detail="Session not found"
        )

    return session