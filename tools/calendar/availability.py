from datetime import timedelta
from config.settings import CALENDAR_EMAIL
from .client import get_calendar_service

CALENDAR_ID = CALENDAR_EMAIL


def is_slot_available(start_time, end_time):
    service = get_calendar_service()

    body = {
        "timeMin": start_time.isoformat(),
        "timeMax": end_time.isoformat(),
        "timeZone": "Asia/Karachi",
        "items": [{"id": CALENDAR_ID}],
    }

    result = service.freebusy().query(body=body).execute()

    busy = result["calendars"][CALENDAR_ID]["busy"]

    return len(busy) == 0


def suggest_slots(requested_time):
    suggestions = []

    offsets = [-60, -30, 30, 60, 90]

    for minutes in offsets:
        new_start = requested_time + timedelta(minutes=minutes)
        new_end = new_start + timedelta(minutes=30)

        if is_slot_available(new_start, new_end):
            suggestions.append(
                new_start.strftime("%I:%M %p")
            )

        if len(suggestions) >= 3:
            break

    return suggestions