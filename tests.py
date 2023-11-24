def get_sum(a,b):
    result = 0
    if a > b:
        a, b = b, a
    elif a == b:
        return b
    while a <= b:
        result += a
        a += 1
    return result

print(get_sum(5,0))
        