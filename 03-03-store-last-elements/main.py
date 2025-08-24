from collections import deque


q1 = deque(maxlen=5)

q1.append(5)
q1.append(4)
q1.append(3)
q1.append(2)
q1.append(1)
print(q1)

q1.append(6)
print(q1)

q1.append(7)
print(q1)

q2 = deque()

q2.append(1)
q2.append(2)
q2.append(3)
print(q2)

print("Append 6 to the left")
q2.appendleft(6)
print(q2)

print("Pop from the right")
q2.pop()
print(q2)

print("Pop from the left")
q2.popleft()
print(q2)


def search(lines, pattern, history=3):
    previous_lines = deque(maxlen=history)

    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


if __name__ == "__main__":
    import os

    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "myfile.txt")

    with open(file_path) as f:
        for line, prevlines in search(f, "python", 2):
            for pline in prevlines:
                print(pline, end="")
            print(line, end="")
            print("-" * 20)
