from itertools import combinations

if __name__ == '__main__':
    text, size = input().split()
    print(*[''.join(j) for i in range(1, int(size)+1) for j in combinations(sorted(text), i)],sep='\n')
