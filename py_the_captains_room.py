k, rooms = int(input()), list(map(int, input().split()))
my_set = set(rooms)
print(((sum(my_set)*k) - sum(rooms))//(k-1))
