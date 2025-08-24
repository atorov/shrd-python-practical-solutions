import statistics


def drop_first_last(grades: list[int]) -> float:
    _first, *middle, _last = grades
    return statistics.mean(middle)


print(drop_first_last([1, 2, 3, 4, 5]))

record = ("Dave", "dave@example.com", "555-1234", "555-5678", "555-8765")
name, email, *phone_numbers = record
print(name)
print(email)
print(phone_numbers)

passwd = "nobody:*:*:*:Nobody:/var/empty:/usr/bin/false"
uname, *fields, homedir, sh = passwd.split(":")
print(uname)
print(fields)
print(homedir)
print(sh)

record = ("Book", 5, 91.71, (12, 24, 2025))
name, *_, (*_, year) = record
print(name)
print(year)
