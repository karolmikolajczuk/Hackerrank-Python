import itertools

if __name__ == '__main__':
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    for cart in itertools.product(A, B):
        print(cart, end=' ')

    
