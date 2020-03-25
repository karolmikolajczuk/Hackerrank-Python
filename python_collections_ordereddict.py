from collections import OrderedDict

list_of_products_with_prices = {}

def manage_products_list(name, price):
    if name in list_of_products_with_prices:
        last_price = list_of_products_with_prices[name]
        list_of_products_with_prices[name] = int(last_price) + price
    else:
        list_of_products_with_prices[name] = price

def print_dict():
    for name in list_of_products_with_prices:
        print('{}{}'.format(name, list_of_products_with_prices[name]))

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        data = input()
        name = []
        price = data.split()[len(data.split())-1]
        for name_ind in range(len(data.split())-1):
            name.append(data.split()[name_ind])
            name.append(" ")

        manage_products_list(''.join(name), int(price))

    print_dict()
