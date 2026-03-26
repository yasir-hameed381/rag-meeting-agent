import dateparser
from datetime import timedelta
from zoneinfo import ZoneInfo

DEFAULT_TZ = ZoneInfo("Asia/Karachi")


def parse_time(user_input: str):
    dt = dateparser.parse(
        user_input,
        settings={
            "PREFER_DATES_FROM": "future",
            "TIMEZONE": "Asia/Karachi",
            "RETURN_AS_TIMEZONE_AWARE": True,
        },
    )

    if not dt:
        return None, None  

    dt = dt.astimezone(DEFAULT_TZ)
    end = dt + timedelta(minutes=30)

    return dt, end