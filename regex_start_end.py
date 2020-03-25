import re

text = input()
target = input()

pattern = re.compile(target)
results = pattern.search(text)
if not results: print("(-1, -1)")
while results:
    print("({0}, {1})".format(results.start(), results.end()-1))
    results = pattern.search(text, results.start()+1)

