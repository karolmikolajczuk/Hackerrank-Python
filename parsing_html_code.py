import re


text = ''

#read each line of input
for _ in range(int(input())):
    #check if this is comment line, then erase it
    text = re.sub(r'<!.+-->',r' ',(text+input()))

#for each found opening tag
for er in re.findall(r'<([^/][^>]*)>', text):
    #if there is a space which means there is some
    #attribute
    if ' ' in er:
        # for each found attribute
        for ere in re.findall(r'([a-z]+)? *([a-z-]+)="([^"]+)', er):
            if ere[0]:
                print(ere[0])
            # print attribute and value
            print('-> '+ere[1]+' > '+ere[2])

    #print tag name
    else:
        print(er)
