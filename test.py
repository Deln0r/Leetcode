def updated(dictionary, **kwargs):
    new = dictionary.copy()
    new.update(kwargs)
    return new

d = {'a': 1, 'b': False}
print(updated(d, misha = 30))