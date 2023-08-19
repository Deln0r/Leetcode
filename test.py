def quarter_of(month):
    if month < 4:
        return 1
    elif month > 3 and month < 7:
        return 2
    elif month > 6 and month < 10:
        return 3
    elif month > 9:
        return 4


list = 7
print(quarter_of(list))
