for i in range(int(input())):
    a, b = input().split()
    try:
        print(int(int(a)//int(b)))
    except ZeroDivisionError as zde:
        print("Error Code:", zde)
    except ValueError as ve:
        print("Error Code:", ve)
