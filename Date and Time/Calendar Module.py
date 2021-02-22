import calendar

def day_name(x):
    day_dict = {
        '0': "MONDAY",
        '1': "TUESDAY",
        '2': "WEDNESDAY",
        '3': "THURSDAY",
        '4': "FRIDAY",
        '5': "SATURDAY",
        '6': "SUNDAY"
    }
    return day_dict[str(x)]

month, day, year = map(int, input().split())
day_of_the_week = calendar.weekday(year, month, day)
print(day_name(day_of_the_week))
