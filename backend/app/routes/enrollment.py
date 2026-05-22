from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.enrollment import Enrollment
from app.models.user import User
from app.schemas.enrollment_schema import EnrollmentCreate

router = APIRouter()


@router.post("/create")
def create_enrollment(
    enrollment: EnrollmentCreate,
    db: Session = Depends(get_db)
):

    # Check if user exists
    user = db.query(User).filter(
        User.id == enrollment.user_id
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    new_enrollment = Enrollment(
        user_id=enrollment.user_id,
        sessions_purchased=enrollment.sessions_purchased,
        total_amount=enrollment.total_amount,
        status="active",
        start_date=enrollment.start_date
    )

    db.add(new_enrollment)
    db.commit()
    db.refresh(new_enrollment)

    return {
        "message": "Enrollment created successfully",
        "data": new_enrollment
    }


@router.get("/")
def get_enrollments(
    db: Session = Depends(get_db)
):

    enrollments = db.query(Enrollment).all()

    return enrollments