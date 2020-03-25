if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

# make it a list map->list
listl = list(arr)

# sort it from max to min
listl.sort(reverse=True)

# check cause it can be a draw at the top
for i in listl:
    if (i != listl[0]):
        print(i)
        break
    
