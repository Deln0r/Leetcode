L = [1,2,3,4,5,6,7,8,9,0]
f1 = [x+1 for x in L]
f2 = (x+1 for x in L)
print(f1)
print(f2)
print(f2.__next__())
print(next(f2))
print(iter(f2))
        