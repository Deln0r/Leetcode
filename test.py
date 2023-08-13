def count_all(data):
    d = {}
    for elem in data:
        d.update({elem: 1})

    return d


print(count_all([1, 2, 3, 3, 2, 4]))




def count_all(items):
    counters = {}
    for item in items:
        counters[item] = counters.get(item, 0) + 1
    return counters
