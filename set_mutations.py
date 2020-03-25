s1_size = int(input())
s1 = set(map(int, input().split()))
for i in range(int(input())):
    command, size_other_set = input().split()
    other_set = set(map(int, input().split()))

    if "intersection_update" in command:
        s1.intersection_update(other_set)
    elif "symmetric_difference_update" in command:
        s1.symmetric_difference_update(other_set)
    elif "difference_update" in command:
        s1.difference_update(other_set)
    else:
        s1.update(other_set)
print(sum(s1))
