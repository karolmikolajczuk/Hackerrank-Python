import itertools

if __name__ == '__main__':
    data, r = input().split()
    results = []
    for output in itertools.permutations(data, int(r)):
        results.append(''.join(list(output)))

    results.sort()
    for text in results:
        print(text)
