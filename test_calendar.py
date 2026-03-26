from tools.calendar.client import get_calendar_service

service = get_calendar_service()

events = service.events().list(
    calendarId='primary',
    maxResults=5
).execute()

print(events)