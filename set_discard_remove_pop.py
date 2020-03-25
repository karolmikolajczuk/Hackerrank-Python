backpack = set()
N = int(input())
backpack = set(map(int, input().split()))

for i in range(int(input())):
    text = input()
    if "pop" in text:
        backpack.pop()
    else:
        command, number = text.split()
        if "remove" in command:
            try:
                backpack.remove(int(number))
            except KeyError as ke:
                pass
        else:
            backpack.discard(int(number))

print(sum(backpack))
