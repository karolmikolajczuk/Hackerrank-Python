import itertools

n = int(input())
letters = input().split()
k = int(input())
paired_letters = list()
count = 0

for pairs in itertools.combinations(letters, k):
    paired_letters.append(pairs)

print(paired_letters)
for pair in paired_letters:
    if 'a' in pair:
        count += 1

print('{0:0.3f}'.format(count/len(paired_letters)))
