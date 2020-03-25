my_set = set(map(int, input().split()))
answer = True
for i in range(int(input())):
    s = set(map(int, input().split()))
    if not (my_set >= s and my_set != s):
        answer = False
        break
print(answer)
