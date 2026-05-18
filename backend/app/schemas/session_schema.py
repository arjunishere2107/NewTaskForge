from pydantic import BaseModel
from datetime import datetime


class SessionCreate(BaseModel):
    user_id: int
    enrollment_id: int

    start_time: datetime
    end_time: datetime

    session_sequence_number: int

    is_trial: bool = False