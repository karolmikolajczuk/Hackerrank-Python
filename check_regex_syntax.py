import re

for i in range(int(input())):
    result = True
    try:
        t = re.compile(input())
    except re.error as reerr:
        result = False
    
    print(result)
