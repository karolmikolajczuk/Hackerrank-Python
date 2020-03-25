def check_if_alnum(s):
    for char in s:
        if char.isalnum():
            return True
    return False

def check_if_alpha(s):
    for char in s:
        if char.isalpha():
            return True
    return False

def check_if_digit(s):
    for char in s:
        if char.isdigit():
            return True
    return False

def check_if_lower(s):
    for char in s:
        if char.islower():
            return True
    return False

def check_if_upper(s):
    for char in s:
        if char.isupper():
            return True
    return False
if __name__ == '__main__':
    s = input()
    print(check_if_alnum(s))
    print(check_if_alpha(s))
    print(check_if_digit(s))
    print(check_if_lower(s))
    print(check_if_upper(s))
