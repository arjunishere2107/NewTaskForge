from pydantic import BaseModel
from datetime import datetime


class ScheduleCreate(BaseModel):

    user_id: int
    enrollment_id: int

    weekday: str

    start_time: datetime
    end_time: datetime

    frequency_per_week: int