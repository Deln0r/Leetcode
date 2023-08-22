# определение функции декоратора
def check(input_func):    
    def output_func(*args):
        name = args[0]
        age = args[1]           # получаем значение второго параметра
        if age < 0: age = 1     # если возраст отрицательный, изменяем его значение на 1
        input_func(name, age)   # передаем функции значения для параметров
    return output_func
 
# определение оригинальной функции
@check
def print_person(name, age):
    print(f"Name: {name}  Age: {age}")
 
# вызов оригинальной функции
print_person("Tom", 38)
print_person("Bob", -5)