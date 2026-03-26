from .client import get_calendar_service
from config.settings import CALENDAR_EMAIL

def book_meeting(start_time, end_time):
    service = get_calendar_service()

    event = {
        "summary": "Technovez Meeting",
        "start": {
            "dateTime": start_time.isoformat(),
            "timeZone": "Asia/Karachi",
        },
        "end": {
            "dateTime": end_time.isoformat(),
            "timeZone": "Asia/Karachi",
        },
        # "attendees": [{"email": email}],
    }

    event = service.events().insert(
        calendarId=CALENDAR_EMAIL,
        body=event
    ).execute()

    return event.get("htmlLink")