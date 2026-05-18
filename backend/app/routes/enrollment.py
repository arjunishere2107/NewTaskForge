from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.enrollment import Enrollment

router = APIRouter()

@router.post("/create")
def create_enrollment(db: Session = Depends(get_db)):

    enrollment = Enrollment(
        user_id=1,
        sessions_purchased=20,
        total_amount=5000,
        status="active"
    )

    db.add(enrollment)
    db.commit()
    db.refresh(enrollment)

    return enrollment