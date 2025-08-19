from datetime import datetime
from pytz import timezone

d = datetime(2025, 12, 15, 9, 30, 0)
print(d)

central = timezone("US/Central")

central_d = central.localize(d)
print(central_d)

bg_d = central_d.astimezone(timezone("Europe/Sofia"))
print(bg_d)
