from email.utils import parseaddr, formataddr
import re

pattern = r'[a-zA-Z]{1}[a-zA-Z0-9._-]*@\w+.[a-zA-Z]{1,3}'
prog = re.compile(pattern)

for i in range(int(input())):
    inp = email.utils.parseaddr(input())
    result = prog.match(inp[1])
    if result:
        print(email.utils.formataddr((inp[0], inp[1])))


