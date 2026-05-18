from pydantic import BaseModel
from datetime import datetime


class SlotCreate(BaseModel):

    instructor_id: int

    start_time: datetime
    end_time: datetime