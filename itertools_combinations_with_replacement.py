from itertools import combinations_with_replacement

if __name__ == '__main__':
    text, size = input().split()
    print(*[''.join(list(tp)) for tp in combinations_with_replacement(sorted(text), int(size))],sep='\n')
