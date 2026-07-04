# 🚀 TaskForge

> **A Production-Ready Learning Management System (LMS) Backend built with FastAPI**

TaskForge is a scalable backend architecture designed for real-world EdTech platforms. It handles the complete lifecycle of students, instructors, scheduling, enrollments, payments, sessions, notifications, and business workflows while following production-grade backend practices.

---

# ✨ Features

## 👨‍🎓 Student Management

- Student Registration & Authentication
- Parent Information Management
- Student Profiles
- Trial Session Support

---

## 📚 Enrollment System

- Purchase Session Packages
- Remaining Session Tracking
- Enrollment Lifecycle Management
- Active / Expired Enrollment Status

---

## 👨‍🏫 Instructor Management

- Instructor Profiles
- Primary Instructor Assignment
- Actual Session Instructor Tracking
- Instructor Availability
- Instructor Slot Management
- Instructor Workload Tracking

---

## 📅 Scheduling Engine

- One-Time Session Booking
- Weekly Recurring Sessions
- Instructor Slot Allocation
- Weekly Session Validation
- Schedule Versioning
- Production Business Rules

---

## 🎯 Session Management

- Session Creation
- Session Completion
- Session Cancellation
- Session Rescheduling
- Trial Sessions
- Makeup Sessions
- Attendance Tracking
- Teacher Notes
- Student Feedback
- Meeting Links

---

## 💳 Payment System

- Payment Records
- Enrollment Linking
- Payment Status Tracking
- Discount Support

---

## 📒 Ledger System

Business events are tracked using ledger-based architecture.

Includes:

- Session Ledger
- Instructor Earnings Ledger
- Teacher Cancellation Ledger
- Future Financial Ledgers

---

## 🔔 Notification System

Designed for:

- Student Notifications
- Parent Notifications
- Instructor Notifications

---

## 📜 Audit Logs

Tracks important business events for:

- Compliance
- Monitoring
- Debugging
- Production Auditing

---

# 🛡️ Production Business Rules

Implemented production-grade validations including:

- Weekly session limits
- Duplicate session prevention
- Session deduction validation
- Completed session protection
- Instructor availability validation
- Past-date booking prevention
- Enrollment validation

---

# 🏗️ Project Structure

```text
backend/
│
├── app/
│   ├── enums/
│   ├── models/
│   ├── routes/
│   ├── schemas/
│   ├── services/
│   ├── utils/
│   ├── database.py
│   └── main.py
│
├── core/
│   ├── config.py
│   ├── database.py
│   └── security.py
│
└── requirements.txt
```

---

# 🛠️ Tech Stack

### Backend

- FastAPI
- SQLAlchemy ORM
- Pydantic
- Uvicorn

### Database

- SQLite (Development)
- SQLAlchemy ORM

### Authentication

- JWT Authentication
- Password Hashing

### Architecture

- Modular API Design
- Service Layer Pattern
- Business Rule Validation
- Ledger-Based Transactions

---

# 📂 Database Models

- User
- Enrollment
- Schedule
- Session
- Instructor
- Instructor Availability
- Instructor Slot
- Session Ledger
- Session Resolution
- Payment
- Notification
- Audit Log
- Instructor Payout
- Instructor Payout Item
- Instructor Earnings Ledger
- Teacher Cancellation Ledger

---

# 🔄 Workflow

```text
Student
    │
    ▼
Enrollment
    │
    ▼
Schedule
    │
    ▼
Instructor Slot
    │
    ▼
Session
    │
    ├────────► Session Ledger
    │
    ├────────► Instructor Earnings
    │
    ├────────► Notifications
    │
    └────────► Audit Logs
```

---

# 🚀 API Modules

- Authentication
- Student Management
- Enrollment Management
- Instructor Management
- Session Management
- Scheduling
- Payments
- Notifications

---

# 💻 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/TaskForge.git
```

Move into the project

```bash
cd TaskForge
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the server

```bash
uvicorn app.main:app --reload
```

---

# 📌 Current Progress

- ✅ Authentication System
- ✅ Student Management
- ✅ Enrollment Module
- ✅ Instructor Management
- ✅ Scheduling Engine
- ✅ Session Management
- ✅ Payment Models
- ✅ Ledger Architecture
- ✅ Notification Models
- ✅ Business Rule Validation

### 🚧 In Progress

- AI-Powered Rescheduling Engine
- Automatic Slot Generator
- Smart Instructor Allocation
- Payment Gateway Integration
- Calendar Integration
- Analytics Dashboard

---

# 🎯 Design Principles

- Production-First Architecture
- Modular Codebase
- Enterprise Scalability
- Business-Driven Workflow Design
- Easy Maintainability
- Extensible Service Layer

---

# 👨‍💻 Author

**Arjun Bhardwaj**

- Python Backend Developer
- AI / LLM Engineer
- FastAPI Developer

GitHub: https://github.com/arjunishere2107

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!!!!!