from langchain.tools import tool
from tools.calendar.booking import book_meeting
from tools.calendar.availability import is_slot_available, suggest_slots
from tools.calendar.utils import DEFAULT_TZ
from tools.calendar.utils import parse_time

@tool
def schedule_meeting_tool(time_str: str) -> str:
    """
    Schedule a meeting. Input should be a natural language time like:
    'tomorrow at 3pm' or 'March 28 at 5pm'
    """

    start_time, end_time = parse_time(time_str)
    if not start_time or not end_time:
        return "❌ Could not understand time."

    if is_slot_available(start_time, end_time):
        link = book_meeting(start_time, end_time)
        return f"✅ Meeting booked at {start_time.strftime('%I:%M %p')}.\n{link}"
    
    suggestions = suggest_slots(start_time)
    if suggestions:
        return (
            "❌ This slot is not available.\n"
            f"👉 Available near times: {', '.join(suggestions)}"
        )

    return "❌ This time slot is not available."