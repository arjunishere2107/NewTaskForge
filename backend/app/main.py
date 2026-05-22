from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine

# ROUTES
import app.routes.auth as auth
import app.routes.instructor as instructor
import app.routes.slot as slot
import app.routes.enrollment as enrollment
import app.routes.session as session_route
import app.routes.dashboard as dashboard

# MODELS
from app.models import (
    user,
    instructor as instructor_model,
    enrollment as enrollment_model,
    instructor_slot,
    session,
    session_ledger
)

# CREATE TABLES
Base.metadata.create_all(bind=engine)

# FASTAPI APP
app = FastAPI(
    title="EdTech Platform API"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# AUTH ROUTES
app.include_router(
    auth.router,
    prefix="/auth",
    tags=["Auth"]
)

# INSTRUCTOR ROUTES
app.include_router(
    instructor.router,
    prefix="/instructors",
    tags=["Instructors"]
)

# SLOT ROUTES
app.include_router(
    slot.router,
    prefix="/slots",
    tags=["Slots"]
)

# ENROLLMENT ROUTES
app.include_router(
    enrollment.router,
    prefix="/enrollments",
    tags=["Enrollments"]
)

# SESSION ROUTES
app.include_router(
    session_route.router,
    prefix="/sessions",
    tags=["Sessions"]
)

# DASHBOARD ROUTES
app.include_router(
    dashboard.router,
    prefix="/dashboard",
    tags=["Dashboard"]
)

# HOME ROUTE
@app.get("/")
def home():
    return {
        "message": "EdTech Platform API Running Successfully"
    }