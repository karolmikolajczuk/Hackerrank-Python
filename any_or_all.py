N, my_list = int(input()), list(map(int, input().split()))
print(all([num > 0 for num in my_list]) and any([str(number) == str(number)[::-1] for number in my_list]))
