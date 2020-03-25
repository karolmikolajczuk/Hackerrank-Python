from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    pass

d = OrderedCounter(input() for _ in range(int(input())))
print(len(d))
print(*d.values())

#################################
def func1(n, list_of_words):
    black_list = []
    count_words = 0
    count_list = []
    for word in list_of_words:
        count = 1
        if word in black_list:
            continue
        else:
            black_list.append(word)
            count_words += 1

        for ind, subword in enumerate(list_of_words):
            if word == subword and list_of_words.index(word) != ind:
                count += 1

        count_list.append(count)

    print(count_words)
    print(' '.join([str(number) for number in count_list]))
#############################
    
##if __name__ == '__main__':
##    n = int(input())
##    list_of_words = [input() for i in range(n)]
##
##    func1(n, list_of_words)

    
    
