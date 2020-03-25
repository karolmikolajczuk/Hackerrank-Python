from itertools import product

# read data
K, M = map(int, input().split())
list_of_lists = list()

# printed result
Smax = 0

# read K lists of numbers
for i in range(K):
    list_of_lists.append(list(map(int, input().split()[1:])))

# create an list of bindings
result = list(product(*list_of_lists))

# for each element of those lists check the equation
for bind in result:
    temp = 0
    for el in bind:
        temp += el**2
    
    if Smax < (temp % M):
        Smax = temp % M

# print result
print(Smax)
    
