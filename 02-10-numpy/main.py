import numpy as np

x = [1, 2, 3, 4]
y = [5, 6, 7, 8]

print(x * 2)
# print(x + 10)  # TypeError: can only concatenate list (not "int") to list
print(x + y)

# Element-wise operations
ax = np.array(x)
ay = np.array(y)

print(ax * 2)
print(ax + 10)
print(ax + ay)
print(ax * ay)
