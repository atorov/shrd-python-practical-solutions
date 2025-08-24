from collections import deque
from collections.abc import Iterable
from typing import Deque, Generator


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


def search(
    lines: Iterable[str], pattern: str, history: int = 3
) -> Generator[tuple[str, Deque[str]], None, None]:
    previous_lines: Deque[str] = deque(maxlen=history)
    for cur_line in lines:
        if pattern in cur_line:
            yield cur_line, previous_lines
        previous_lines.append(cur_line)


if __name__ == "__main__":
    import os

    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "myfile.txt")

    with open(file_path, encoding="utf-8") as f:
        for line, prev_lines in search(f, "python", 2):
            for pline in prev_lines:
                print(pline, end="")
            print(line, end="")
            print("-" * 20)
