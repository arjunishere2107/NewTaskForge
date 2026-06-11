from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine

# =========================
# IMPORT ENUMS (IMPORTANT)
# =========================
from app.enums.session_status import SessionStatus
from app.enums.payment_status import PaymentStatus
from app.enums.schedule_status import ScheduleStatus
from app.enums.slot_status import SlotStatus

# =========================
# ROUTES
# =========================
import app.routes.auth as auth
import app.routes.instructor as instructor
import app.routes.slot as slot
import app.routes.enrollment as enrollment
import app.routes.session as session_route
import app.routes.availability as availability
import app.routes.dashboard as dashboard
import app.routes.schedule as schedule_route

# =========================
# MODELS
# IMPORTANT:
# Import ALL models here
# so SQLAlchemy can detect them
# before create_all()
# =========================
from app.models import (
    user,
    instructor as instructor_model,
    enrollment as enrollment_model,
    instructor_slot,
    session,
    session_ledger,
    schedule,

    # NEW CORE MODELS
    payment,
    notification,
    audit_log,
    session_resolution,
    instructor_availability,
    instructor_earning_ledger,
    instructor_payout,
    instructor_payout_item,
    teacher_cancellation_ledger,
)

# =========================
# CREATE DATABASE TABLES
# =========================
Base.metadata.create_all(bind=engine)

# =========================
# FASTAPI APP
# =========================
app = FastAPI(
    title="EdTech Platform API",
    description="Production-grade EdTech Scheduling & Session Management Backend",
    version="1.0.0"
)

# =========================
# CORS CONFIG
# =========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# AUTH ROUTES
# =========================
app.include_router(
    auth.router,
    prefix="/auth",
    tags=["Auth"]
)

# =========================
# INSTRUCTOR ROUTES
# =========================
app.include_router(
    instructor.router,
    prefix="/instructors",
    tags=["Instructors"]
)

# =========================
# SLOT ROUTES
# =========================
app.include_router(
    slot.router,
    prefix="/slots",
    tags=["Slots"]
)

# =========================
# ENROLLMENT ROUTES
# =========================
app.include_router(
    enrollment.router,
    prefix="/enrollments",
    tags=["Enrollments"]
)

# =========================
# SESSION ROUTES
# =========================
app.include_router(
    session_route.router,
    prefix="/sessions",
    tags=["Sessions"]
)

# =========================
# AVAILABILITY ROUTES
# =========================
app.include_router(
    availability.router,
    prefix="/availability",
    tags=["Availability"]
)

# =========================
# DASHBOARD ROUTES/HOME ROUTE
# =========================
app.include_router(
    dashboard.router,
    prefix="/dashboard",
    tags=["Dashboard"]
)

# =========================
# SCHEDULE ROUTES
# =========================
app.include_router(
    schedule_route.router,
    prefix="/schedules",
    tags=["Schedules"]
)

# =========================
# HEALTH CHECK
# =========================
@app.get("/")
def home():
    return {
        "message": "EdTech Platform API Running Successfully",
        "version": "1.0.0",
        "status": "healthy"
    }

# =========================
# ENUM TEST ROUTE
# Helps verify enums working
# =========================
@app.get("/system/enums")
def get_enums():
    return {
        "session_status": [status.value for status in SessionStatus],
        "payment_status": [status.value for status in PaymentStatus],
        "schedule_status": [status.value for status in ScheduleStatus],
        "slot_status": [status.value for status in SlotStatus],
    }