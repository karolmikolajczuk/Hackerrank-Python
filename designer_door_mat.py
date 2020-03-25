dash = '-'
dot = '.'
pipe = '|'
welcome = 'WELCOME'
signature = dot + pipe + dot


def print_welcome(N, M):
    #wrong data
    if N*3 != M:
        return
    #print door
    for row in range(N+1):
        #for col in range(M):
        #check if this is middle
        if row == (int(N/2)+1):
            x = int((M - len(welcome)) / 2)
            print(dash*x + welcome + dash*x)
            continue

        #check if this is second half
        elif row > (int(N/2)+1):
            y = int((N-row)*2 + 1)
            x = int((M-(len(signature)*y)) / 2)
            print(dash*x + signature*y + dash*x)

        #check if this is first half
        elif row < int(N/2):
            y = int(row*2 + 1)
            x = int((M-(len(signature)*y))/2)
            print(dash*x + signature*y + dash*x)
            continue



if __name__ == '__main__':
    N, M = map(int, input().split())
    print(N)
    print(M)
    print(type(N))
    print(type(M))
    print_welcome(N, M)    
