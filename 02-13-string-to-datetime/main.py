from datetime import datetime
import locale

text = "2023-10-01 12:30:45"

y = datetime.strptime(text, "%Y-%m-%d %H:%M:%S")
print(y)

z = datetime.now()
print(z)

diff = z - y
print(diff)

formatted_z = z.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_z)

formatted_z2 = datetime.strftime(z, "%Y-%m-%d %H:%M:%S")
print(formatted_z2)

try:
    locale.setlocale(locale.LC_ALL, "bg_BG")
except locale.Error:
    print("Error: Locale not supported!")

formatted_z3 = datetime.strftime(z, "%A, %d %B %Y")
print(formatted_z3)


def parse_ymd(date_string: str) -> datetime:
    """
    Parse a date string in the format YYYY-MM-DD.
    Return a datetime object.
    Raise ValueError if the format is invalid.
    """
    try:
        year, month, day = map(int, date_string.split("-"))
        return datetime(year, month, day)
    except ValueError as exp:
        raise ValueError(
            f'Error: Invalid date format! "{date_string}" - {exp}'
        ) from exp


print(parse_ymd("2025-10-01"))
