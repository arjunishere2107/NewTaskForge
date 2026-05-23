from datetime import datetime

def is_session_missed(session):

    if (
        session.status == "scheduled"
        and session.end_time < datetime.utcnow()
    ):
        return True

    return False
