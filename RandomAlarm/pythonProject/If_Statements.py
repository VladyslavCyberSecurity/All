from os import symlink

from sympy import prime
from sympy.physics.units import temperature

from variables import year_of_birth

num = int(input("1. Введіть число: "))
if num % 2 == 0:
    print("Число парне")
else:
    print("Число непарне")
print("----------------")

point = int(input("2. Введіть бал: "))
if 90 <= point <= 100:
    print("Відмінно")
elif point > 100:
    print("Помилка, введіть число від 0 до 100")
elif point >= 75:
    print("Добре")
elif point >= 50:
    print("Задовільно")
elif point >= 0:
    print("Погано")
elif point < 0:
    print("Помилка, введіть число від 0 до 100")
print("----------------")

a = int(input("3. Введіть перше число: "))
b = int(input("Введіть друге число: "))
if a > b:
    print("Максимум:", a, ", ", "Мінімум:", b)
elif b > a:
    print("Максимум:", b, ", ", "Мінімум:", a)
elif a == b:
    print("Числа рівні")
print("----------------")

client_age = int(input("4. Введіть свій вік: "))
if client_age < 18:
    print("Ви неповнолітній")
elif 18 <= client_age <= 65:
    print("Ви дорослий")
elif 66 <= client_age <= 100:
    print("Ви пенсіонер")
elif client_age > 100:
    print("Пахне побріхеньками")
print("----------------")

password = "Bandera1909"
enter_password = input("5. Введіть пароль: ")
if enter_password == password:
    print("Доступ дозволено")
else:
    print("Доступ заборонено")
print("----------------")

num = int(input("6. Введіть число: "))
if num > 0:
    print("Позитивне")
elif num < 0:
    print("Негативне")
else:
    print("0")
print("----------------")

year = int(input("7. Введіть рік: "))
if year % 400 == 0:
    print("Переносний")
elif year % 100 == 0:
    print("Не переносний")
elif year % 4 == 0:
    print("Переносний")
else:
    print("Не переносний")
print("----------------")

login = "Daryn_Sultan"
password = "IloveBandera1909"
login_input = input("8. Введіть логін: ")
password_input = input("Введіть пароль: ")
if login_input == login and password_input == password:
    print("Вхід дозволено")
elif login_input == login and password_input != password:
    print("Пароль невірний")
elif login_input != login and password_input == password:
    print("Логін невірний")
elif login_input != login and password_input != password:
    print("Немає доступу")
print("----------------")

a = int(input("9. Введіть перше число: "))
b = int(input("Введіть друге число: "))
c = int(input("Введіть третє число: "))
if a > b > c:
    print("Найбільше число: ", a, "Найменше число: ", c)
elif a > c > b:
    print("Найбільше число: ", a, "Найменше число: ", b)
elif b > a > c:
    print("Найбільше число: ", b, "Найменше число: ", c)
elif b > c > a:
    print("Найбільше число: ", b, "Найменше число: ", a)
elif c > a > b:
    print("Найбільше число", c, "Найменше число: ", b)
elif c > b > a:
    print("Найбільше число", c, "Найменше число: ", a)
elif a == b and b == c and a == c:
    print("Числа рівні")
elif a == b and c < a and c < b:
    print("Числа a i b рівні:", a, "=", b,".", "Найменше число c =", c)
elif a == c and b < a and b < c:
    print("Числа a i c рівні:", a, "=", c,".", "Найменше число b =", b)
elif b == c and a < b and a < c:
    print("Числа b i c рівні:", b, "=", c,".", "Найменше число a =", a)
print("----------------")

sum_purchase = int(input("10. Введіть суму покупки: "))
if sum_purchase > 1000:
    print("Знижка 10%! Сума: ", sum_purchase - sum_purchase * 0.1)
elif 500 <= sum_purchase <= 1000:
    print("Знижка 5%! Сума: ", sum_purchase - sum_purchase * 0.05)
elif sum_purchase < 500:
    print("Знижки немає. Сума:", sum_purchase)
print("----------------")

a = int(input("11. Введіть довжину першої сторони: "))
b = int(input("Введіть довжину другої сторони: "))
if a == b:
    print("Це квадрат")
else:
    print("Це прямокутник")
print("----------------")

temperature = int(input("12. Введіть температуру: "))
if temperature < 0:
    print("Мороз")
elif 0 <= temperature <= 20:
    print("Прохолодно")
elif 21 <= temperature <= 30:
    print("Тепло")
elif temperature > 30:
    print("Спека")
print("----------------")

month = int(input("13. Введіть номер місяця: "))
if month in (12, 1, 2):
    print("Зима")
elif month in (3, 4, 5):
    print("Весна")
elif month in (6, 7, 8):
    print("Літо")
elif month in (9, 10, 11):
    print("Осінь")
else:
    print("Помилка: введи число від 1 до 12")
print("----------------")

password = input("14. Введіть пароль:")
if len(password) < 6:
    print("Занадто короткий")
elif password == "qwerty":
    print("Пароль занадто простий")
else:
    print("Пароль прийнято")
print("----------------")

num = int(input("15. Введіть число: "))
if 10 <= num <= 50:
    print("У діапазоні")
elif num < 10:
    print("Занадто маленьке")
elif num > 50:
    print("Занадто велике")
print("----------------")

theory = int(input("16. Введіть бал за теорію: "))
practice = int(input("Введіть бал за практику: "))
if theory >= 50 and practice >= 50:
    print("Складено")
elif theory >= 50 and practice < 50:
    print("Потрібна перездача")
elif theory < 50 and practice >= 50:
    print("Потрібна перездача")
elif theory < 50 and practice < 50:
    print("Не складено")
print("----------------")

color = input("17. Ведіть колір: ")
if color == "red":
    print("Stop")
elif color == "yellow":
    print("Wait")
elif color == "green":
    print("Go")
else:
    print("An unknown signal")
print("----------------")

a = int(input("18. Введіть число: "))
if a % 2 == 0 and 0 <= a <= 100:
    print("Парне у діапазоні")
elif a % 2 == 0 and a > 100:
    print("Парне, але велике")
else:
    print("Непарне число")
print("----------------")

a = int(input("19. Введіть першу сторону: "))
b = int(input("Введіть другу сторону: "))
c = int(input("Введіть третю сторону: "))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Рівносторонній трикутник")
    elif a == b or a == c or b == c:
        print("Рівнобічний трикутник")
    else:
        print("Різносторонній трикутник")
else:
    print("Трикутник не існує")
print("----------------")

import random
num = random.randint(1,5)
print('Випало число ' + str(num))
if num == 3:
  print('Вгадав')
elif num > 3:
    print('Завелике')
elif num < 3:
    print('Замале')
print("----------------")

secret = 3
guess = int(input("20. Вгадай число (від 1 до 5): "))
if guess == secret:
    print("Вгадав!")
elif guess > secret:
    print("Завелике")
else:
    print("Замале")
print("----------------")

year_of_birth = int(input("21. Введіть свій вік: "))
if year_of_birth < 18:
    print("Доступ заборонено")
else:
    print("Доступ дозволено")
print("----------------")

num = int(input("22. Введіть число: "))
if num > 0:
    print("Позитивне")
elif num < 0:
    print("Негативне")
else:
    print("Нуль")
print("----------------")

month = input("23. Введіть місяць: ")
if month.lower() in ("грудень", "січень", "лютий"):
    print("Зима")
elif month.lower() in ("березень", "квітень", "травень"):
    print("Весна")
elif month.lower() in ("червень", "липень", "серпень"):
    print("Літо")
elif month.lower() in ("вересень", "жовтень", "листопад"):
    print("Осінь")
else:
    print("Невідомий місяць")
print("----------------")

password = input("24. Введіть пароль: ")
if len(password) < 6:
    print("Закороткий")
elif password == "123456" or password == "qwerty":
    print("Занадто простий")
else:
    print("Надійний")
print("----------------")

a = int(input("25. Введіть перше число = "))
b = int(input("Введіть друге число = "))
if a > b:
    print("Перше більше")
elif b > a:
    print("Друге більше")
else:
    print("Рівні")
print("----------------")

num = int(input("26. Введіть число: "))
if num % 2 == 0 and 1 <= num <=100:
    print("Парне у діапазоні")
elif num % 2 == 0 and num > 100:
    print("Парне, але велике")
else:
    print("Непарне")
print("----------------")

word = input("27. Введіть слово: ")
if 'a' in word.lower():
    print("Містить 'а'")
else:
    print("Не містить 'а'")
print("----------------")

day_of_week = input("28. Введіть день тижня: ")
if day_of_week.lower() == ["Субота", "Неділя"]:
    print("Вихідний")
else:
    print("Робочий")
print("----------------")

year = int(input("29. Введіть рік: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 !=0):
    print("Переносний рік")
else:
    print("Звичайний рік")
print("----------------")

mark = int(input("30. Введіть оцінку від 1 до 12: "))
if 10 <= mark <= 12:
    print("Відмінно")
elif mark in ( 7, 8, 9):
    print("Добре")
elif mark in ( 4, 5, 6):
    print("Задовільно")
elif mark in (1, 2, 3):
    print("Погано")
else:
    print("ВВЕДІТЬ ЧИСЛО ВІД 1 ДО 12!!!!")
print("----------------")

num = int(input("31. Введіть число: "))
if num % 3 == 0:
    print("Дільник 3", end=" ")
    if num % 5 == 0:
        print("і 5")
elif num % 5 == 0:
    print("Дільник 5")
else:
    print("Не ділиться ні на 3, ні на 5")
print("----------------")

letter = input("32. Введіть літеру: ")
#if "а" or "е" or "и" or "і" or "о" or "у" or "ю" or "я" in letter:
if letter.lower() in "аеииоуюя":
    print("Голосна")
else:
    print("Приголосна")
print("----------------")

a = int(input("33. Введіть перше число: "))
b = int(input("Введіть друге число: "))
c = int(input("Введіть третє число: "))
if a > b and a > c:
    print("Найбільше число а: ", a)
elif b > a and b > c:
    print("Найбільше число b: ", b)
else:
    print("Найбільше число c: ", c)
print("----------------")

days = [
    "Понеділок",
    "Вівторок",
    "Середа",
    "Четвер",
    "П’ятниця",
    "Субота",
    "Неділя"
]
num = int(input("34. Введіть день тижня від 1 до 7: "))
if 1 <= num <= 7:
    print(days[num - 1])   # мінус 1, бо індексація починається з 0
else:
    print("Невірний день")
print("----------------")
days = {
    1: "Понеділок",
    2: "Вівторок",
    3: "Середа",
    4: "Четвер",
    5: "П’ятниця",
    6: "Субота",
    7: "Неділя"
}
num = int(input("Введіть день тижня від 1 до 7: "))
print(days.get(num, "Невірний день"))
print("----------------")

year = int(input("35. Введіть рік: "))
if year % 4 == 0 and year % 100 != 0:
    print("Святковий рік")
else:
    print("Звичайний рік")
print("----------------")

num = int(input("36. Введіть число: "))
if num % 2 == 0:
    print("Парне")
else:
    print("Непарне")
print("----------------")

word = input("37. Введіть слово: ")
if len(word) > 5:
    print("Містить більше 5 символів")
else:
    print("Коротке")
print("----------------")

num = int(input("38. Введіть число: "))
if num < 0 and num % 2 !=0:
    print("Від’ємне і непарне")
elif num < 0 and num % 2 == 0:
    print("Від’ємне і парне")
elif num > 0 and num % 2 != 0:
    print("Додатнє і непарне")
else:
    print("Додатнє і парне")
print("----------------")

num_of_month = {
    1: "січень",
    2: "лютий",
    3: "березень",
    4: "квітень",
    5: "травень",
    6: "червень",
    7: "липень",
    8: "серпень",
    9:  "вересень",
    10:"жовтень",
    11:"листопад",
    12: "грудень"
}
month = int(input("39. Введіть місяць: "))
print(num_of_month.get(month, "Невідомий місяць"))
print("----------------")

theory = int(input("40. Введіть оцінку за теорію: "))
practice = int(input("40. Введіть оцінку за практику: "))
if theory >= 50 and practice >= 50:
    print("Складено")
elif theory >= 50 or practice >= 50:
    print("Потрібна перездача")
else:
    print("Не складено")
print("----------------")

character = input("41. Enter a character: ")
if character.lower() in "aeiou":
    print("Vowel")
else:
    print("Consonant")
print("----------------")

weekend = ["Saturday", "Sunday"]
day = input("42. Enter a day of week: ")
if day in weekend:
    print("Weekend")
else:
    print("Weekday")
print("----------------")

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_check = int(input("43. Enter number: "))
if list_check in list_of_numbers:
    print("Inside range")
else:
    print("Out of range")
print("----------------")

punctuation_characters = {".", ",", "!", "?"}
characters = input("44. Enter character: ")
if characters in punctuation_characters:
    print("Yeaah")
else:
    print("Noooooooooo")
print("----------------")

dictionary_mapping = {
    "(": "parenthesis",
    "[": "square bracket",
    "{": "curly brace"
}
char = input("45. Enter dict: ")
print (dictionary_mapping.get(char, "not a bracket"))
print("----------------")

character = {
    "(",
    "[",
    "{"
}
char = input("46. Enter char: ")
if char in character:
    print("Contains opening bracket")
else:
    print ("not a bracket")
print("----------------")

num = int(input("47. Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0 and num % 5 != 0:
    print("Fizz")
elif num % 5 == 0 and num % 3 != 0:
    print("Buzz")
else:
    print("No match")
print("----------------")

year = int( input("48. Enter year: "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Leap year")
else:
    print("blablabla")
print("----------------")

word = input("49. Enter a word: ")
if 5 <= len(word) <=10:
    print("Medium length")
elif len(word) < 5:
    print("Too short")
else:
    print("Too long")
print("----------------")

a = int(input("50. Enter first number: "))
b = int(input("Enter second number: "))
#if a % 2 == 0 and b % 2 == 0:
#    print("Both even")
#elif a % 2 != 0 and b % 2 != 0:
#    print("Both odd")
if a % 2 == b % 2:
    print("Both even" if a % 2 == 0 else "Both odd")
else:
    print("Mixed")
print("----------------")