from tools.calendar.utils import parse_time
from tools.calendar.availability import (
    is_slot_available,
    suggest_slots
)
from tools.calendar.booking import book_meeting


def handle_meeting_request(user_input: str, email="rh6666358@gmail.com"):
    print(f"Received meeting request: {user_input}")
    start, end = parse_time(user_input)

    print(f"Parsed time: {start} to {end}")
    if not start:
        return "❌ I couldn't understand the time. Please specify like 'tomorrow 3pm'."

    if is_slot_available(start, end):
        link = book_meeting(start, end, email)
        return f"✅ Meeting booked successfully!\n{link}"

    suggestions = suggest_slots(start)

    if suggestions:
        return (
            "❌ This slot is not available.\n"
            f"👉 Available near times: {', '.join(suggestions)}"
        )

    return "❌ No nearby slots available."