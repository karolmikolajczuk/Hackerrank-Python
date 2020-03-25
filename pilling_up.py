tests = int(input())
for i in range(tests):
    n_cubes = int(input())
    cubes = list(map(int, input().split()))

    descending = True
    count_of_changes = 0
    for cube_ind in range(n_cubes-1):
        if not descending and cubes[cube_ind] > cubes[cube_ind+1]:
            count_of_changes += 1
            descending = True
        elif descending and cubes[cube_ind] < cubes[cube_ind+1]:
            count_of_changes += 1
            descending = False
            
    if count_of_changes <= 1:
        print("Yes")
    else:
        print("No")
