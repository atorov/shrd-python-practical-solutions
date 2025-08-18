from datetime import datetime, timedelta

a = timedelta(days=3, hours=6)
b = timedelta(hours=2.5)

c = a + b
print(c)
print(c.days)
print(c.seconds)
print(c.seconds / 3600)
print(c.total_seconds() / 3600)

d = datetime.now()
print(d)

d2 = datetime.today()
print(d2)

e = datetime(2017, 12, 22)
print(e)
print(e + timedelta(days=10))

f = datetime(2025, 1, 1)
print(f)

g = f - e
print(g)
print(g.days)
print(g + timedelta(minutes=5))
