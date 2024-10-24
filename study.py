###################### ИЩЕМ УНИКАЛЬНЫЙ ЭЛЕМЕНТ
# s = "abracadabrax"
# def search(s):
#     d = {}
#     for ch in s:
#         if ch in d:
#             d[ch] += 1
#         else:
#             d[ch] = 1
#     for k in d:
#         if d[k] == 1:
#             return k
# print(search(s))


# gen = (i+1 for i in range(10))
# print(lis)
# dic = {i : i*2 for i in range(10)}
# print(dic)

##################### БИНПОИСК В ЧАСТИЧНО РАЗВЁРНУТОМ СПИСКЕ
# l = [4,5,1,2,3]
# def search_rotated_list(nums, target):

#     left, right = 0, len(nums) - 1

#     while left <= right:
#         mid = (left + right) // 2

#         if nums[mid] == target:
#             return mid

#         # Проверяем, в какой половине находится target
#         if nums[left] <= nums[mid]:  # Левая половина отсортирована
#             if nums[left] <= target < nums[mid]:
#                 right = mid - 1
#             else:
#                 left = mid + 1
#         else:  # Правая половина отсортирована
#             if nums[mid] < target <= nums[right]:
#                 left = mid + 1
#             else:
#                 right = mid - 1

#     return -1  # Элемент не найден



#     for i, num in enumerate(nums):  # Проходим по списку с индексами
#         if num == target:
#             return i

#     return -1  # Элемент не найден

############################# УНИКАЛЬНЫЙ ЭЛЕМЕНТ В СОРТ.СПИСКЕ ДУБЛЕЙ
# def find_single_element(nums):

#     left, right = 0, len(nums) - 1  # Инициализация левой и правой границ поиска
#     while left < right:  # Пока границы не сошлись
#         mid = left + (right - left) // 2  # Вычисление среднего индекса

#         # Проверка четности/нечетности индекса mid
#         if mid % 2 == 0:  # Если mid четный
#             if nums[mid] == nums[mid + 1]:  # Пара найдена, уникальный элемент справа
#                 left = mid + 2  # Сдвигаем левую границу
#             else:  # Уникальный элемент слева
#                 right = mid  # Сдвигаем правую границу
#         else:  # Если mid нечетный
#             if nums[mid] == nums[mid - 1]:  # Пара найдена, уникальный элемент справа
#                 left = mid + 1  # Сдвигаем левую границу
#             else:  # Уникальный элемент слева
#                 right = mid - 1  # Сдвигаем правую границу

#     return nums[left]  # Возвращаем единственный элемент


############################## КЛАССИЧЕСКИЙ БИНАРНЫЙ ПОИСК
# l = [i+10 for i in range(40)]
# n = 32
# def bin_search(my_list, num):
#     l, r = 0, len(my_list)-1
#     while l <= r:
#         mid = (l+r) // 2
#         if my_list[mid] == num:
#             return mid
#         elif my_list[mid] > num:
#             r = mid - 1
#         else:
#             l = mid + 1
#     return -1
# print(bin_search(l, n))


# slice = [1]

# def is_monotonic (slice):
#     inc = dec = True
#     for i in range(1, len(slice)):
#         if slice[i] < slice[i -1]:
#             inc = False
#         if slice[i] > slice[i -1]:
#             dec = False
#     return inc or dec

# print(is_monotonic(slice))


# def atm_withdraw(amount, banknotes):
#     """
#     Симулирует работу банкомата. Выдает запрашиваемую сумму, если возможно.
    
#     :param amount: Запрашиваемая сумма.
#     :param banknotes: Словарь с номиналами купюр и их количеством.
#     :return: Обновленный словарь с купюрами или ошибка.
#     """
#     # Создаем копию словаря для расчетов, чтобы не изменять оригинал до подтверждения выдачи
#     temp_banknotes = banknotes.copy()
    
#     # Список номиналов в порядке убывания для удобства выдачи крупных купюр сначала
#     denominations = sorted(temp_banknotes.keys(), reverse=True)
    
#     for denomination in denominations:
#         if amount <= 0:
#             break
        
#         # Максимальное количество купюр данного номинала, которые можно выдать
#         count_to_give = min(amount // denomination, temp_banknotes[denomination])
        
#         # Уменьшаем количество купюр данного номинала в временном словаре
#         temp_banknotes[denomination] -= count_to_give
#         amount -= denomination * count_to_give
    
#     if amount > 0:
#         return "Ошибка: невозможно выдать запрашиваемую сумму"
    
#     # Обновляем оригинальный словарь
#     banknotes.update(temp_banknotes)
#     return banknotes

# # Пример использования
# banknotes = {5000: 2, 500: 1, 1000: 3, 200: 0}
# amount = 7500
# result = atm_withdraw(amount, banknotes)
# print(result)  # Ожидаемый результат: {5000: 1, 500: 0, 1000: 3, 200: 0}

# amount = 10000
# result = atm_withdraw(amount, banknotes)
# print(result)  # Ожидаемый результат: Ошибка: невозможно выдать запрашиваемую сумму

# apple = [5,5,5]
# capacity = [2,4,2,7]


# def minimumBoxes(apple, capacity):
#     n = sum(apple)
#     c = 0

#     capacity.sort(reversed=True)

#     for i in range(len(capacity)):
#         c += capacity[i]
#         if c >= n:
#             return i

# print(minimumBoxes(apple, capacity))

import re

def is_palindrome(word):
    return word == word[::-1]

def analyze_text(text):
    # Заменяем тире, дефисы и прочие символы, приводим к нижнему регистру
    text = re.sub(r'[–—-]', ' ', text)  # тире и дефисы на пробелы
    text = re.sub(r'(?<=[а-яА-Яa-zA-Z])(?=\.)', '. ', text)  # добавляем пробел после точки, если его нет
    text = re.sub(r'[^\w\s]', '', text)  # убираем все символы, кроме букв, цифр и пробелов
    text = text.lower()
    
    # Разделяем текст на слова, игнорируя двойные пробелы
    words = text.split()

    # Убираем слова короче 3 символов
    words = [word for word in words if len(word) >= 3]

    total_count = len(words)  # Общее количество слов
    unique_count = len(set(words))  # Количество уникальных слов
    palindrome_count = sum(1 for word in words if is_palindrome(word))  # Количество палиндромов

    return f"Total: {total_count}, Unique: {unique_count}, Palindrome: {palindrome_count}"

text = """
Python — это язык программирования, который стал очень популярным за последние годы. Его простота и гибкость привлекают как новичков, так и опытных разработчиков. Начнем с того, что Python поддерживает множество парадигм, включая императивное, объектно-ориентированное и функциональное программирование.Это позволяет программистам выбирать подход, который наиболее подходит для конкретной задачи. Одним из преимуществ Python является его обширная стандартная библиотека, которая облегчает выполнение различных...
"""

result = analyze_text(text)
print(result)


