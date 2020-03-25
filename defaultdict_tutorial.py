from collections import defaultdict

n, m = tuple(map(int, input().split()))
my_dict = defaultdict(list)

for i in range(n):
    my_dict[input()].append(str(int(i+1)))
for i in range(m):
    question = input()
    if len(my_dict[question]) == 0:
        print("-1")
    else:
        print(' '.join(my_dict[question]))
