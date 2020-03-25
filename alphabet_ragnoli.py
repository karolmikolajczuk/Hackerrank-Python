#ascii start since 97 = 'a'
a_char = 97
dash = '-'

def compute_width(size):
    return size+((size-1)*3)

def create_middle(alphas):
    right = '-'.join(alphas)
    l_list = []
    for i in range(1, len(alphas)):
        l_list.append(alphas[len(alphas)-i])
        left = '-'.join(l_list)

    return left + '-' + right

def create_row_first_half(alphas, row_nr, col_max):
    left = ''
    middle = ''
    right = ''

    #first create char and dash combination substring
    available_chars = row_nr+1 #how many chars are available for use
    list_of_chars = []

    #how many chars from outside
    for ind in range(len(alphas)-1, len(alphas)-available_chars, -1):
        list_of_chars.append(alphas[ind])
    for ind in range(len(alphas)-available_chars, len(alphas)):
        list_of_chars.append(alphas[ind])
    middle = '-'.join(list_of_chars)
    
    #from whole space subtract middle size and divide by two
    rest = int((col_max - len(middle)) / 2)

    #left dash times rest
    left = '-' * rest
    
    #right dash times rest
    right = '-' * rest
    
    return left + middle + right

def create_row_second_half(alphas, row_nr, col_max, size):
    left = ''
    middle = ''
    right = ''

    #first create char and dash combination substring
    available_chars = size - (row_nr-(size-1)) #how many chars are available for use
    list_of_chars = []

    for ind in range(len(alphas)-1, len(alphas)-available_chars, -1):
        list_of_chars.append(alphas[ind])
    for ind in range(len(alphas)-available_chars, len(alphas)):
        list_of_chars.append(alphas[ind])
    middle = '-'.join(list_of_chars)
    
    #from whole space subtract middle size and divide by two
    rest = int((col_max - len(middle)) / 2)

    #left dash times rest
    left = '-' * rest
    
    #right dash times rest
    right = '-' * rest

    return left + middle + right

def print_rangoli(size):
    #create list with char's
    alphas = []
    for char in range(a_char, a_char+size):
        alphas.append(chr(char))

    #columns
    cols = compute_width(size)

    #rows
    rows = (size * 2) - 1

    for row in range(rows):
        #check if middle
        if row == size-1:
            print(create_middle(alphas))

        #check if first half
        if row < size-1:
            print(create_row_first_half(alphas, row, cols))            

        #check if second half
        if row > size-1:
            print(create_row_second_half(alphas, row, cols, size))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
