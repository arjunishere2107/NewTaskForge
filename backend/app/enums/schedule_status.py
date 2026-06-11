from enum import Enum


class ScheduleStatus(str, Enum):
    ACTIVE = "active"
    PAUSED = "paused"
    ENDED = "ended"
    REPLACED = "replaced"