def swap_case(s):
    new_string = []
    for char in s:
        if char.islower():
            new_string.append(char.upper())
        elif char.isspace():
            new_string.append(char)
        else:
            new_string.append(char.lower())
    return ''.join(new_string)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
