from .client import get_calendar_service

def book_meeting(start_time, end_time, email):
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
        calendarId="rh6666358@gmail.com",
        body=event
    ).execute()

    return event.get("htmlLink")