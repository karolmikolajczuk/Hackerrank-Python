for i in range(int(input())):
    n_A, A = int(input()), set(map(int, input().split()))    
    n_B, B = int(input()),set(map(int, input().split()))

    print(A.issubset(B))
