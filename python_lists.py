my_list = []

def which_command(com, param1=0, param2=0):
    if com in 'insert':
        my_list.insert(param1, param2)
    elif com in 'print':
        print(my_list)
    elif com in 'remove':
        my_list.remove(param1)
    elif com in 'append':
        my_list.append(param1)
    elif com in 'sort':
        my_list.sort()
    elif com in 'pop':
        my_list.pop()
    elif com in 'reverse':
        my_list.reverse()
    else:
        print("Error motherfucker")
    

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        nr1 = 0
        nr2 = 0
        buffor = input()
        
        if len(buffor.split()) == 3:
            command, nr1, nr2 = buffor.split()
        elif len(buffor.split()) == 2:
            command, nr1 = buffor.split()
        else:
            command = buffor
        
        which_command(command, int(nr1), int(nr2))
