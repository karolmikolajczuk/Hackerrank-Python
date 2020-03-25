import string

def print_rangoli(size):
    #compute width taking advantage from size
    width = 4*size - 3

    #get all available characters
    alpha = string.ascii_lowercase

    #for each empty space from size-1 to 0 + list from 1 to size-1
    for i in list(range(size))[::-1] + list(range(1, size)):

        #print specific characters with `-` and take that and set it
        #in the middle and put dashes to the left and right if there
        #is some empty space
        print('-'.join(alpha[size-1:i:-1] + alpha[i:size]).center(width, '-'))

if __name__ == '__main__':
    size = int(input())
    print_rangoli(size)
