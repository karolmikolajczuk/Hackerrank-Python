def count_substring(string, sub_string):
    count_ = 0
    for index in range(len(string)):
        if string[index:index+len(sub_string)] == sub_string:
            count_ = count_ + 1

    return count_

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
