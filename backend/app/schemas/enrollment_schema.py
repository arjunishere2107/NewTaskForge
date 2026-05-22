from pydantic import BaseModel
from datetime import datetime


class EnrollmentCreate(BaseModel):

    user_id: int
    sessions_purchased: int
    total_amount: float
    start_date: datetime