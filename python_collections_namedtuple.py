from collections import namedtuple
n, titles = int(input()), input().split()
Students = namedtuple('Students', titles)
print((sum([int(Students._make(input().split()).MARKS) for _ in range(n)]) / n))
