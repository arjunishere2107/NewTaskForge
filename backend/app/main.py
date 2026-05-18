from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine

# Routes
import app.routes.auth as auth
import app.routes.instructor as instructor
import app.routes.slot as slot
import app.routes.enrollment as enrollment

# ONLY keep this if session.py exists
import app.routes.session as session_route

# Models
from app.models import (
    user,
    instructor as instructor_model,
    enrollment as enrollment_model,
    instructor_slot,
    session,
    session_ledger
)

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="EdTech Platform API"
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Auth Routes
app.include_router(
    auth.router,
    prefix="/auth",
    tags=["Auth"]
)

# Instructor Routes
app.include_router(
    instructor.router,
    prefix="/instructors",
    tags=["Instructors"]
)

# Slot Routes
app.include_router(
    slot.router,
    prefix="/slots",
    tags=["Slots"]
)

# Enrollment Routes
app.include_router(
    enrollment.router,
    prefix="/enrollments",
    tags=["Enrollments"]
)

# Session Routes
app.include_router(
    session_route.router,
    prefix="/sessions",
    tags=["Sessions"]
)

# Home Route
@app.get("/")
def home():
    return {
        "message": "EdTech Platform API Running"
    }