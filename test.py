def filter_map(func, items):
    list = []
    for item in items:
        bull, value = func(item)
        if bull is True:
            list += value
        else:
            continue
    print(type(list))
    return list
