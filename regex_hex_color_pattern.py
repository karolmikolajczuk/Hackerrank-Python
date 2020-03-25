import re

for i in range(int(input())):
    for elem in re.findall(r'[\s:](#{1}[0-9a-f]{3,6})', input(), re.I):
        print(elem)
    
