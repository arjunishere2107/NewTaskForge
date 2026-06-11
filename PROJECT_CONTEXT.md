# TaskForge Backend - Project Context Document

## Project Overview

TaskForge is a session-based learning platform where students purchase learning plans and attend scheduled sessions with instructors.

The system manages:

* Students
* Parents
* Instructors
* Schedules
* Sessions
* Payments
* Notifications
* Instructor payouts
* Session resolutions
* Audit logs

Backend Stack:

* FastAPI
* SQLAlchemy ORM
* SQLite (current)
* JWT Authentication
* Alembic (planned/recommended)

---

# Core Business Flow

## Student Journey

1. Student registers
2. Trial session may be scheduled
3. Parent purchases a learning plan
4. Enrollment is created
5. Recurring schedule is generated
6. Sessions are created
7. Instructor conducts session
8. Session gets completed
9. Remaining session balance decreases
10. Feedback collected

---

# Weekly Session Rules

Maximum:

* 2 sessions per student per week

Validation service:

app/services/session_rules.py

Main function:

validate_weekly_limit()

Used in:

* Create Session
* Create Recurring Sessions
* Reschedule Session

Rule:

A student cannot have more than 2 scheduled sessions within the same calendar week.

---

# Session System

Model:

app/models/session.py

Important Fields:

id
user_id
enrollment_id
schedule_id

primary_instructor_id
assigned_instructor_id

start_time
end_time

status

is_trial

is_makeup_session

is_deducted

rescheduled_from_session_id

reschedule_type

feedback_submitted

teacher_notes

student_feedback

---

# Session Status Values

scheduled

live

completed

cancelled

rescheduled

no_show

---

# Instructor Assignment Logic

Every session stores:

primary_instructor_id

Original instructor

assigned_instructor_id

Actual instructor taking class

These may differ when rescheduling.

---

# Schedule System

Model:

app/models/schedule.py

Represents recurring pattern.

Fields:

day_of_week

slot_start_time

slot_end_time

sessions_per_week

start_date

end_date

status

---

# Enrollment System

Model:

app/models/enrollment.py

Represents purchased plan.

Stores:

sessions_purchased

remaining_sessions

payment information

plan lifecycle

One enrollment may generate many sessions.

---

# Instructor Slot System

Model:

app/models/instructor_slot.py

Represents available instructor timeslots.

Fields:

id

instructor_id

start_time

end_time

session_id

is_booked

status

status values:

available

booked

blocked

Important:

status and is_booked must always remain synchronized.

---

# Session Ledger

Model:

app/models/session_ledger.py

Used to track:

session completed

deductions

refunds

manual adjustments

Every session completion creates ledger entry.

---

# Rescheduling System

Three-option architecture.

---

## Option 1

Same-Day Same Instructor

Student may move class to another available slot on the same day.

Conditions:

* Same instructor only
* Same day only
* Must use generated valid slots
* Buffer rules enforced

Session:

assigned_instructor_id remains unchanged

reschedule_type:

same_instructor

---

## Option 2

Same-Day Different Instructor

Student may choose another instructor.

Conditions:

* Same day only
* Any instructor
* Slot must be available

System chooses instructor automatically.

reschedule_type:

different_instructor

assigned_instructor_id changes

primary_instructor_id remains unchanged

---

## Option 3

Defer To End Of Plan

Session moved to final available recurring position.

Conditions:

* Same instructor
* Preserve weekly schedule pattern
* Preserve weekly session limits
* Always available

Creates:

is_makeup_session=True

reschedule_type="deferred"

---

# Buffer Rules

Session Duration:

30 minutes

Buffer:

15 minutes

Effective Slot Usage:

45 minutes

No session may violate buffer constraints.

---

# Current Database Models

Implemented:

User

Enrollment

Instructor

InstructorAvailability

InstructorSlot

Schedule

Session

SessionLedger

Payment

Notification

AuditLog

SessionResolution

InstructorPayout

InstructorPayoutItem

InstructorEarningLedger

TeacherCancellationLedger

---

# Authentication

Current:

JWT based

Routes:

/auth/login

/auth/register

Future:

Forgot Password

Reset Password

Refresh Token

Email Verification

---

# Pending Features

## High Priority

1. Three-option rescheduling system

2. Forgot Password Flow

3. Reset Password Flow

4. Feedback Form

5. Admin Course Management

6. Module Management

7. Lesson Management

8. Course Thumbnails

9. Module Thumbnails

10. Instructor Auto Allocation Engine

---

# Instructor Allocation Strategy

When multiple instructors are available:

Priority:

1. Active instructor
2. Trained instructor
3. Lowest workload
4. Earliest available

Future service:

app/services/instructor_allocator.py

---

# Important Files

Routes

app/routes/auth.py

app/routes/session.py

Services

app/services/session_rules.py

Future:

app/services/reschedule_service.py

app/services/slot_service.py

Models

app/models/*

Core

app/core/config.py

app/core/database.py

app/core/security.py

---

# Production Rules

Completed sessions cannot be rescheduled.

Sessions cannot be scheduled in the past.

Weekly limit must be enforced.

Session deductions must never happen twice.

Instructor slots must never overlap.

Session and slot records must remain synchronized.

---

# Current Development Status

Completed:

Authentication

User model

Instructor model

Enrollment model

Schedule model

Session model

Weekly limit validation

Session completion logic

Ledger integration

Basic rescheduling endpoint

In Progress:

Feedback system

Forgot password

Reset password

add fire base

Admin course management


