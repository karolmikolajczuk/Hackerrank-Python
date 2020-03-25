from collections import deque

n = int(input())
deq = deque()
for i in range(n):
    text = input()
    if "popleft" in text:
        deq.popleft()
    elif "pop" in text:
        deq.pop()
    else:
        command, nr = text.split()
        if command == "appendleft":
            deq.appendleft(nr)
        else:
            deq.append(nr)

for el in deq:
    print(el, end=' ')
