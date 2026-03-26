from langchain.tools import tool
from tools.calendar.booking import book_meeting
from tools.calendar.availability import is_slot_available
from tools.calendar.utils import DEFAULT_TZ
from datetime import datetime, timedelta

@tool
def schedule_meeting_tool(time_str: str) -> str:
    """
    Schedule a meeting. Input should be a natural language time like:
    'tomorrow at 3pm' or 'March 28 at 5pm'
    """

    from dateparser import parse

    dt = parse(
        time_str,
        settings={
            "TIMEZONE": "Asia/Karachi",
            "RETURN_AS_TIMEZONE_AWARE": True,
            "PREFER_DATES_FROM": "future",
        },
    )

    if not dt:
        return "❌ Could not understand time."

    start = dt.astimezone(DEFAULT_TZ)
    end = start + timedelta(minutes=30)

    if is_slot_available(start, end):
        link = book_meeting(start, end, "rh6666358@gmail.com")
        return f"✅ Meeting booked at {start.strftime('%I:%M %p')}.\n{link}"

    return "❌ This time slot is not available."