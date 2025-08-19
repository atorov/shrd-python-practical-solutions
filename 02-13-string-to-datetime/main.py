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

locale.setlocale(locale.LC_ALL, "bg_BG")

formatted_z3 = datetime.strftime(z, "%A, %d %B %Y")
print(formatted_z3)


def parse_ymd(date_string: str) -> datetime:
    year_s, mon_s, day_s = date_string.split("-")
    return datetime(int(year_s), int(mon_s), int(day_s))


print(parse_ymd("2025-10-01"))
