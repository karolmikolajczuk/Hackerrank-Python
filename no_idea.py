n, m = map(int, input().split())
n_array = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
happiness = 0
for number in n_array:
    if number in A:
        happiness += 1
    elif number in B:
        happiness -= 1

print(happiness)
