class MyClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"MyClass instance with value: {self.value}"

    def __repr__(self):
        return f"MyClass({self.value})"
    
man = MyClass(13222)
print(man)