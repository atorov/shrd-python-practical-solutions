import random

values = [1, 2, 3, 4, 5, 6]
print(values)

print(random.choice(values))
print(random.choice(values))
print(random.choice(values))

print(random.sample(values, 2))
print(random.sample(values, 2))
print(random.sample(values, 3))

random.shuffle(values)
print(values)
random.shuffle(values)
print(values)
random.shuffle(values)
print(values)

print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))

print(random.random())
print(random.random())
print(random.random())

print(random.getrandbits(1))
print(random.getrandbits(2))
print(random.getrandbits(8))
print(random.getrandbits(16))
print(random.getrandbits(32))
print(random.getrandbits(64))
print(random.getrandbits(128))
print(random.getrandbits(256))
