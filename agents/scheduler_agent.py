from tools.calendar.utils import parse_time
from tools.calendar.availability import (
    is_slot_available,
    suggest_slots
)
from tools.calendar.booking import book_meeting


def handle_meeting_request(user_input: str):
    print(f"Received meeting request: {user_input}")
    start_time, end_time = parse_time(user_input)

    print(f"Parsed time: {start_time} to {end_time}")
    if not start_time or not end_time:
        return "❌ I couldn't understand the time. Please specify like 'tomorrow 3pm'."

    if is_slot_available(start_time, end_time):
        link = book_meeting(start_time, end_time)
        return f"✅ Meeting booked successfully!\n{link}"

    suggestions = suggest_slots(start_time)

    if suggestions:
        return (
            "❌ This slot is not available.\n"
            f"👉 Available near times: {', '.join(suggestions)}"
        )

    return "❌ No nearby slots available."