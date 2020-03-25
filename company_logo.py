from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    pass

for c in OrderedCounter(sorted(input())).most_common(3): print(*c)
