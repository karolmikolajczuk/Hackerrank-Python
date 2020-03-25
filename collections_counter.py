from collections import Counter

X = int(input())
shoe_sizes = Counter(list(map(int, input().split())))
N = int(input())
collected_money = 0
for customer in range(N):
    desired_shoe, price = tuple(map(int, input().split()))
    if desired_shoe in shoe_sizes.keys() and shoe_sizes[desired_shoe] > 0:
        collected_money += price
        shoe_sizes[desired_shoe] -= 1
    
print(collected_money)
