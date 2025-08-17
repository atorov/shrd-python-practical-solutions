from decimal import Decimal

a = 4.2
b = 3.1
n1 = a + b
print(n1)
print((a + b) == 7.3)

a = Decimal("4.2")
b = Decimal("3.1")
n2 = a + b
print(n2)
print((a + b) == Decimal("7.3"))

x = 47064.52 - 1775.28 - 16456 - 6000 - 350 - 1368 - 13072.5 - 8028.85
print(x)

a = Decimal("47064.52")
b = Decimal("1775.28")
c = Decimal("16456")
d = Decimal("6000")
e = Decimal("350")
f = Decimal("1368")
g = Decimal("13072.5")
h = Decimal("8028.85")
x = a - b - c - d - e - f - g - h
print(x)
