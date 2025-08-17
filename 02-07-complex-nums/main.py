import cmath

a = complex(1, 5)
print(a)
print(a.real)
print(a.imag)
print(a.conjugate())

b = 2 - 5j
print(b)
print(b.real)
print(b.imag)
print(b.conjugate())

print(a + b)
print(a - b)
print(a * b)
print(a / b)

print(cmath.sin(a))
print(cmath.sqrt(b))
