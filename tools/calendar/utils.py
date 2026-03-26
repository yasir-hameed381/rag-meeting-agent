import dateparser
from datetime import timedelta
from zoneinfo import ZoneInfo

DEFAULT_TZ = ZoneInfo("Asia/Karachi")


def parse_time(time_str: str):
    dt = dateparser.parse(
        time_str,
        settings={
            "PREFER_DATES_FROM": "future",
            "TIMEZONE": "Asia/Karachi",
            "RETURN_AS_TIMEZONE_AWARE": True,
        },
    )

    if not dt:
        return None, None  

    start_time = dt.astimezone(DEFAULT_TZ)
    end_time = start_time + timedelta(minutes=30)

    return start_time, end_time