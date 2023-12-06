import itertools, operator

list1 = {1, 3, 5}
res = itertools.accumulate(list1)
print('default:')
for x in res:
    print(x)


res = itertools.accumulate(list1, operator.mul)
print('multiply:')
for x in res:
    print(x)