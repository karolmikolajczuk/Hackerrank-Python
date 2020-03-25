def solve(string):
    return ' '.join([name.capitalize() for name in string.split(' ')])

if __name__ == '__main__':
    string = input()
    print(solve(string))
