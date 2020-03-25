if __name__ == '__main__':
    n = int(input())
    integer_map = map(int, input().split())
    
    tp = tuple(list([int(x) for x in integer_map]))
    #print(tp)
    print(hash(tp))
