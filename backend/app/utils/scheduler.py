from datetime import timedelta

def generate_recurring_dates(
    start_date,
    weeks
):

    dates = []

    current = start_date

    for _ in range(weeks):

        dates.append(current)

        current += timedelta(days=7)

    return dates