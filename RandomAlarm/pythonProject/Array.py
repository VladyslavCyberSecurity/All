nums = []
for i in range(5):
    n = int(input("Введи число: "))
    nums.append(n)
print("Сума:", sum(nums))
print("-----------------")

numbers = [4, 17, 9, 23, 5]
print("Найбільше:", max(numbers))
print("Найменше:", min(numbers))
print("-----------------")

import random
nums = [random.randint(0, 100) for _ in range(10)]
print("Усі числа:", nums)
even_nums = [x for x in nums if x % 2 == 0]
print("Парні:", even_nums)
print("-----------------")

items = input("Введи елементи через пробіл: ").split()
print("Зворотний список:", items[::-1])
print("-----------------")

my_list = ['apple', 'banana', 'kiwi', 'orange']
elem = input("Що шукаємо? ")
if elem in my_list:
    print("Знайдено!")
else:
    print("Немає у списку.")
print("-----------------")

#1
fruits = ['banana', 'kiwi', 'apple', 'pear', 'ananas']
index = int(input("Введіть індекс(0-4): "))
print("На цій позиції:", fruits[index])
new_name = input("Введіть нову назву для цього фрукта: ")
fruits[index] = new_name
print("Оновлений список: ", fruits)
#2
city = ['lviv', 'kyiv', 'ternopil', 'dnipro']
index = int(input("Вкажіть позицію для вставки(0-3): "))
new_city = input("Вкажіть нове місто: ")
city.insert(index, new_city)
print("Новий список: ", city)
print("Кількість міст: ", len(city))
#3
buy_list = ['хліб', 'банани', 'борошно', 'чіпси']
index = int(input("Введіть номер позиції для видалення: "))
if 0 <= index < len(buy_list):
    removed = buy_list.pop(index)
    print(f"Видалено: {removed}")
    print("Оновлений список:", buy_list)
else:
    print("Неправильний індекс!")
#4
names = ['kaka', 'baba', 'mama', 'nana', 'dada']
to_remove = input("Введіть ім'я для видалення: ")
if to_remove in names:
    names.remove(to_remove)        # видаляємо за значенням
    print(f"Видалено: {to_remove}")
    print("Оновлений список:", names)
else:
    print("Не знайдено такого імені!")
#5
lasts_name = ['bob', 'lol', 'kok', 'pop', 'dod']
search_name = input("Введіть ім'я: ")
for name in lasts_name:             # ітеруємо напряму по значеннях
    if name == search_name:
        print(f"Found {search_name}!")
        break
else:
    # цей блок виконається, якщо цикл завершився без break
    print("Ім'я не знайдено.")
#6
#список завдань
task_manager = ['eat','sleep','repeat']

#меню в якому можна вибрати завдання
menu = [
    'read', #показати справу за номером
    'update', #змінити її текст
    'insert', #додати нову
    'remove', #видалити
    'length', #показати кількість справ
    'loop', #показати всі справи
]

print(f'Меню операцій: {menu}') #висвітити всі можливі операції

task = input("Виберіть операцію: ")#ввести операцію
if task in menu: #я писав був for тому всі завдання виконувалися по порядку, змінив на if
    if task == 'read':
        index = int(input("Введіть індекс(read): "))#всюди написав в дужках завдання, щоб слідкувати, що саме виконується
        print("На цій позиції:", task_manager[index])

    elif task == 'update':
        index = int(input("Введіть індекс(update): "))
        new_name = input("Введіть нову справу: ")
        task_manager[index] = new_name
        print("Оновлений список: ", task_manager)

    elif task == 'insert':
        index = int(input("Введіть індекс(insert): "))
        insert = input("Введіть нове значення: ")
        task_manager.insert(index, insert)
        print("Новий список: ", task_manager)

    elif task == 'remove':
        to_remove = input("Введіть значення(remove): ")
        task_manager.remove(to_remove)
        print(f"Видалена справа: {to_remove}")
        print("Оновлений список: ", task_manager)

    elif task == 'length':
        print("Кількість справ(len): ", len(task_manager))

    elif task == 'loop':
        for item in task_manager:
            print(item, end=' ')#end, щоб все було в ряд і пустота в дужках для пробілу
    else:
        print("Невідома операція")
#6(2)
task_manager = ['eat', 'sleep', 'repeat']

menu = [
    'read',
    'update',
    'insert',
    'remove',
    'length',
    'loop',
    'exit'
]

print(f'Меню операцій: {menu}')

while True:
    task = input("\nВиберіть операцію: ").strip().lower()

    if task == 'read':
        index = int(input("Введіть індекс: "))
        if 0 <= index < len(task_manager):
            print("На цій позиції:", task_manager[index])
        else:
            print("Невірний індекс.")

    elif task == 'update':
        index = int(input("Введіть індекс: "))
        if 0 <= index < len(task_manager):
            new_name = input("Нова справа: ")
            task_manager[index] = new_name
            print("Оновлений список:", task_manager)
        else:
            print("Невірний індекс.")

    elif task == 'insert':
        index = int(input("Введіть індекс: "))
        if 0 <= index <= len(task_manager):
            new_task = input("Нова справа: ")
            task_manager.insert(index, new_task)
            print("Новий список:", task_manager)
        else:
            print("Невірний індекс.")

    elif task == 'remove':
        to_remove = input("Введіть значення: ")
        if to_remove in task_manager:
            task_manager.remove(to_remove)
            print(f"Видалено: {to_remove}")
        else:
            print("Такої справи немає.")
        print("Поточний список:", task_manager)

    elif task == 'length':
        print("Кількість справ:", len(task_manager))

    elif task == 'loop':
        for item in task_manager:
            print(item, end=' ')
        print()

    elif task == 'exit':
        print("Завершення роботи.")
        break

    else:
        print("Невідома операція.")
#7
empty = []
for num in range(0, 21):        # від 0 до 20 включно
    if num % 2 == 0:            # перевіряємо парність
        empty.append(num)       # додаємо число, не True/False
print(empty)
#8
# 1. Збираємо слова в список
words = []
while True:
    w = input("Введи слово (Enter – кінець): ")
    if w == "":
        break
    words.append(w)
# 2. Виводимо у зворотному порядку без reverse()
# Варіант А: цикл for у зворотному напрямку
for i in range(len(words) - 1, -1, -1):
    print(words[i])
#9
grades = [7, 9, 10, 6, 8]
first_index = int(input())
second_index = int(input())
new_value1 = int(input())
new_value2 = int(input())
grades[first_index] = new_value1
grades[second_index] = new_value2
print(grades)
#10
nums = [1, 2, 2, 3, 1, 4, 3]
unique = []
for n in nums:
    if n not in unique:
        unique.append(n)
print(unique)
print(len(unique))
#11
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(num[0], num[-1])
#12
num = [1, 3, 4, 5, 6]
index = len(num)//2
num[2] = index
print(num)
#13
arr = []
while True:
    num = input("GIVE ME NUM (or 'stop' to finish): ")
    if num.lower() == 'stop':
        break
    else:
        try:
            value = int(num)
            arr.append(value)
        except ValueError:
            print("NO NUM")
print("Your list:", arr)
#14
letters = ['a', 'b', 'c', 'd', 'e']
value = '#'
letters.insert(0, value)
print(letters)
#15
fruits = ['banana', 'apple', 'pineapple', 'coconut']
fruits.pop(1)
fruits.pop()
print(fruits)
#16
word = ['kaka', 'wawa', 'papa', 'dada', 'caca', 'vava', 'baba']
count = 0
for i in word:
    if 'a' in i:
        print(i)
        count += 1
print("words with 'a':", count)
#17
arr = []
while len(arr) < 10:
    num = input("enter nums: ")
    try:
        value = int(num)
        arr.append(value)
    except ValueError:
        print("not num")
even_sum = 0
for n in arr:
    if n % 2 == 0:
        even_sum += n
print("Your list:", arr)
print("sum of even numbers:", even_sum)
#18
first_list = ['anna', 'andrey', 'mark', 'mathew']
second_list = ['anna', 'lala', 'petro', 'mark']
new_list = []
# Додаємо елементи з першого списку
for name in first_list:
    if name not in new_list:
        new_list.append(name)
# Додаємо елементи з другого списку
for name in second_list:
    if name not in new_list:
        new_list.append(name)
print("Об'єднаний список без повторів:", new_list)
#19
arr = ['afs', 'sg', 'dhrtg', 'sga', 'cxvn']
for i in range(len(arr)-1, -1, -1):
    print(arr[i])
#20
arr = []

while True:
    command = input("Enter command (add, del, show, exit): ").lower()

    if command == 'exit':
        break

    elif command == 'add':
        value = input("Enter value to add: ")
        arr.append(value)

    elif command == 'del':
        try:
            index = int(input("Enter index to delete: "))
            if 0 <= index < len(arr):
                arr.pop(index)
            else:
                print("Invalid index!")
        except ValueError:
            print("Please enter a number!")

    elif command == 'show':
        print("Your list:", arr)

    else:
        print("Unknown command!")

#21, 22
fruits = ['apple', 'banana', 'coconut', 'ananananana']
print(fruits[0])
print(fruits[-1])
#23
arr = [1, 3, 6, 5, 2]
arr[len(arr)//2] = 100
print(arr)
#24, 25
arr = [1, 3, 6, 5, 2]
value = int(input("1.: "))
arr.insert(len(arr), value)
value2 = int(input("2.: "))
arr.insert(0, value2)
print(arr)
#26
arr = ['baba', 'gaga', 'sasa', 'xaxa']
value = input("Value for delete: ")
if value in arr:
    arr.remove(value)
    print(arr)
#27
arr2 = ['lala', 'pala', 'fala', 'xaxa']
arr2.pop(1)
print(arr2)
#28
arr3 = ['zaza', 'tata', 'wawa', 'xaxa']
print(len(arr3))
#29
arr4 = ['qaqa', 'eaea', 'gaga', 'xaxa']
for x in arr4:
    print(x)
#30
arr = [1, 2 ,3, 4, 5]
value = int(input("enter num: "))
if value in arr:
    print('found')
#31
from asyncio import current_task

arr = [1,2,5,6,8,2,9,3]
total = 0
for number in arr:
    if number % 2 == 0:
        total += number
print("Sum: ", total)
#32
nums = [1,3,2,6,1,3,6,3]
new_list = []
for x in nums:
    if x not in new_list:
        new_list.append(x)
print(new_list)
#33
arr = [1,2,3]
for i in range(len(arr)-1, -1, -1):
    print(arr[i], end=' ')
#34
tasks = ['kurwa', 'qwerty', 'idk', 'lol']

while True:
    command = input("Command (add, del, show, exit): ").lower()

    if command == 'exit':
        break

    elif command == 'add':
        new_task = input("Enter new task: ")
        tasks.append(new_task)

    elif command == 'del':
        try:
            index = int(input("Index to delete: "))
            if 0 <= index < len(tasks):
                tasks.pop(index)
            else:
                print("Invalid index!")
        except ValueError:
            print("Please enter a number!")

    elif command == 'show':
        print("Tasks:", tasks)

    else:
        print("Unknown command!")

#35
arr = [1, 2, 3]
current_max = arr[0]         # стартуємо з першого елемента
for value in arr:
    if value > current_max:
        current_max = value
print(current_max)
#36
numbers = [3,7,2,9]
print(numbers[0])
print(numbers[-1])
#37
num = [5,8,3,7,9]
index = len(num)//2
num[index] = 100
print(num)
#38
arr = [1,2,3]
try:
    num = int(input("Enter number: "))
    arr.append(num)
    print(arr)
except ValueError:
    print("pls ent a vld integer")
#39
a = [1,2,3,4]
num = int(input("Enter number: "))
a.insert(0, num)
print(a)
#40
words = ["cat","dog","bird"]
w = input("Enter word to remove: ").strip()
if w in words:
    words.remove(w)
    print("Removed:", w)
else:
    print("Word not found.")
print(words)
#41
arr = ["cat","dog","bird"]
try:
    idx = int(input("Index: "))
    removed = arr.pop(idx)
    print("Removed:", removed)
    print(arr)
except ValueError:
    print("Enter a number!")
except IndexError:
    print("Index out of range!")

#42
words = ["cat","dog","bird"]
print(len(words))
#43
arr = ["cat","dog","bird"]
for item in arr:
    print(item, end=' ')
print()
#44
arr = [1,2,3,2,5,6,3]
num = int(input("Enter number: "))
if num in arr:
    print("Found")
else:
    print("Not found")
#45
arr = [1,2,3,2,5,6,3]
total = 0
for n in arr:
    if n%2==0:
        total+=n
print(total)
#46
nums = [1, 2, 3, 2, 4, 2, 5]
x = int(input("Яке число порахувати? "))
print("Кількість входжень:", nums.count(x))
print("-----------------")
#47
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
merged = list(set(a + b))
print("Об’єднаний без дублювань:", merged)
print("-----------------")
#48
nums = [10, 20, 30, 40]
average = sum(nums) / len(nums)
print("Середнє:", average)
print("-----------------")
#49
words = ["pear", "apple", "banana", "kiwi"]
print("За абеткою:", sorted(words))
print("За довжиною:", sorted(words, key=len))
print("-----------------")
#50
nums = [1, 2, 2, 3, 4, 4, 5]
unique = []
for n in nums:
    if n not in unique:
        unique.append(n)
print("Унікальні:", unique)
print("-----------------")