from fractions import Fraction


a = Fraction(2, 4)
print(a)
print(type(a))

b = Fraction(8, 16)
print(b)
print(type(b))

print(a + b)

c = a * b
print(c)
print(type(c))
print(c.numerator)
print(c.denominator)

print(float(c))

x = 4.75
y = Fraction(*x.as_integer_ratio())
print(y)
print(type(y))
