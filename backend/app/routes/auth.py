from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.schemas.user_schema import UserCreate, UserLogin
from app.utils.auth import create_access_token

router = APIRouter()


# =========================
# SIGNUP
# =========================
@router.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):

    # Check existing phone
    existing_user = (
        db.query(User)
        .filter(User.phone == user.phone)
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Phone number already exists"
        )

    # Create user
    new_user = User(
        phone=user.phone,
        email=user.email,

        student_name=user.student_name,
        student_age=user.student_age,

        parent_name=user.parent_name,
        parent_phone=user.parent_phone,

        # Trial system
        trial_status="not_started",

        # User status
        status="active"
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # JWT Token
    token = create_access_token({
        "id": new_user.id,
        "phone": new_user.phone
    })

    return {
        "message": "User created successfully",
        "access_token": token,
        "token_type": "bearer"
    }


# =========================
# LOGIN
# =========================
@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    existing_user = (
        db.query(User)
        .filter(User.phone == user.phone)
        .first()
    )

    if not existing_user:
        raise HTTPException(
            status_code=400,
            detail="Invalid phone number"
        )

    # Later Firebase OTP verification will happen here

    token = create_access_token({
        "id": existing_user.id,
        "phone": existing_user.phone
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }