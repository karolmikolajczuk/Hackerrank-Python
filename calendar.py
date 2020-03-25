import calendar

month, day, year = map(int, input().split())

calendar.setfirstweekday(calendar.MONDAY)
result = calendar.weekday(year, month, day)

if result == 0:
    print("MONDAY")
elif result == 1:
    print("TUESDAY")
elif result == 2:
    print("WEDNESDAY")
elif result == 3:
    print("THURSDAY")
elif result == 4:
    print("FRIDAY")
elif result == 5:
    print("SATURDAY")
else:
    print("SUNDAY")
    
