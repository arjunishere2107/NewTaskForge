from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db

from app.models.instructor import Instructor

from app.schemas.instructor_schema import InstructorCreate

router = APIRouter()


# CREATE INSTRUCTOR
@router.post("/")
def create_instructor(
    instructor: InstructorCreate,
    db: Session = Depends(get_db)
):

    existing_instructor = (
        db.query(Instructor)
        .filter(Instructor.phone == instructor.phone)
        .first()
    )

    if existing_instructor:
        raise HTTPException(
            status_code=400,
            detail="Instructor already exists"
        )

    new_instructor = Instructor(
        name=instructor.name,
        phone=instructor.phone,
        email=instructor.email,
        type=instructor.type,
        is_active=True,
        is_trained=True
    )

    db.add(new_instructor)
    db.commit()
    db.refresh(new_instructor)

    return {
        "message": "Instructor created successfully",
        "data": new_instructor
    }


# GET ALL INSTRUCTORS
@router.get("/")
def get_instructors(db: Session = Depends(get_db)):

    instructors = db.query(Instructor).all()

    return instructors


# GET SINGLE INSTRUCTOR
@router.get("/{instructor_id}")
def get_instructor(
    instructor_id: int,
    db: Session = Depends(get_db)
):

    instructor = (
        db.query(Instructor)
        .filter(Instructor.id == instructor_id)
        .first()
    )

    if not instructor:
        raise HTTPException(
            status_code=404,
            detail="Instructor not found"
        )

    return instructor