from pandas.io.sas.sas_constants import text_block_size_length
from pygments.lexer import words
from sympy.physics.units import current, length
from torch.distributions.constraints import square
from unicodedata import digit

a = 5
b = 2
a, b = b, a
print("1.", "a=", a, "b=", b)
print("----------------")

year_of_birth = 2004
current_year = 2025
age = current_year - year_of_birth
print("2.", "Тобі", age, "років")
print("----------------")

salary_per_hour = 128
hours = 176
total_salary = salary_per_hour * hours
print("3.", "Зарплата за місяць", total_salary, "грн")
print("----------------")

text = 'Vladyslav'
length = len(text)
print("4.", "У моєму імені", length, "букв")
print("----------------")

x = 5
y = 2
z = 3
avg = (x + y + z) / 3
print("5.", "Середнє значення: ", avg)
print("----------------")

celsius = 20
fahrenheit = (celsius * (9 / 5)) + 32
print("6.", celsius, "°C", "=", fahrenheit, "°F")
print("----------------")

street = "Shevchenka"
city = "Lviv"
house_number = 10
full_address =  city + ", " + street + " " + str(house_number)
print("7.", full_address)
print("----------------")

num = 10
double_num = num * 2
print("8.", "Подвоєне число:", double_num)
print("----------------")

sentence = "З днем відновлення незалежности України!"
num_chars = len(sentence)
num_words = len(sentence.split())
print("9.","Кількість символів:", num_chars, "Кількість слів:", num_words)
print("----------------")

a = 10
b = 2
print("10.", "Сума:", a+b, "Різниця:", a-b, "Добуток:", a*b, "Частка:",  a/b)
print("----------------")

a = 10
b = 4
P = 2 * (a+b)
S = a * b
print("11.","Периметр:", P, "Площа:", S)
print("----------------")

mark1 = 5
mark2 = 3
mark3 = 5
avg = (mark1 + mark2 + mark3)/3
print("12.", "Середній бал:", avg)
print("----------------")

seconds = 135
minutes = seconds // 60
remaining_seconds = seconds % 60
print("13.", minutes, "хв", remaining_seconds, "сек")
print("----------------")

first_name = "Vladyslav"
last_name = "Izhevskyi"
full_name = last_name + " " + first_name
print("14.", full_name)
print("----------------")

uah = 5000
usd_rate = 41.37
exchange = uah / usd_rate
print("15.", uah, "грн", "=" , round(exchange, 2), "$")
print("----------------")

import math
radius = 7
S = math.pi * radius**2
print("16.","Площа кола:", round(S, 2))
print("----------------")

age = 21
current_year = 2025
hundred_year = current_year - age + 100
print("17.", "Тобі буде 100 років у", hundred_year, "році")
print("----------------")

distance = 120
time = 2
U = distance / time
print("18.", "Середня швидкість:", U)
print("----------------")

num = 12345
last_digit = num % 10
print("19.", "Остання цифра числа:", last_digit)
print("----------------")

side = 4
V = side**3
print("20.", "Об'єм куба:", V)
print("----------------")

num = 1234
sum_digit = num%10 + num//10%10 + num//100%10 + num//1000%10
print("21.", "Сума всіх цифр:", sum_digit)
print("----------------")

name = "vladyslav"
name_corrected = name.capitalize()
print("22.", name_corrected)
print("----------------")

a = 10
b = 5
if a > b:
    print('23. a >')
else:
    print('23. b >')
print("----------------")

fahrenheit = 451
celsius = (fahrenheit - 32) * 5/9
print("24.", "Температура Фаренгейта у Цельсії:", round(celsius, 2), "C")
print("----------------")

num = 10
if num % 2 == 0:
    print('25. Число парне')
else:
    print('25. Число непарне')
print("----------------")

num = 5000
divided_num = num // 100
print("26.", divided_num)
print("----------------")

a = 10
b = 5
c = 7
if a > b and a > c:
    print("27. Найбільше число = ", a)
elif b > a and b > c:
    print("27. Найбільше число = ", b)
else:
    print("27. Найбільше число = ", c)
print("----------------")

word = "Україна"
num_chars = len(word)
print("28.", num_chars)
print("----------------")

a = -5
if a > 0:
    print("29. Позитивне")
elif a < 0:
    print("29. Негативне")
elif a == 0:
    print("29. Нуль")
print("----------------")

sentence = "Привіт, Владиславе!"
sentence_upper = sentence.upper()
print("30.", sentence_upper)
print("----------------")

a = 5
square = a ** 2
cube = a ** 3
print("31.", "Квадрат:", square, "Куб:", cube)
print("----------------")

num = 12345
last_num = num%10
first_num = num//10000%10
numnum = first_num + last_num
print("32.", numnum)
print("----------------")

first_name = "Владислав"
last_name = "Іжевський"
full_name = last_name + ", " + first_name
print("33.", full_name)
print("----------------")

word = "Python"
word_reverse = word[::-1]
print("34.", word_reverse)
print("----------------")

a = 15
if a % 3 == 0 and a % 5 == 0:
    print("35. True")
else:
    print("35. False")
print("----------------")

num = 4567
num_digit = num // 1000
print("36.", num_digit)
print("----------------")

num = 100
if num > 100:
    print("37. Число більше 100")
elif num < 100:
    print("37. Число менше 100")
else:
    print("37. Число дорівнює 100")
print("----------------")

sentence_1 = "Python"
sentence_2 = "Programming"
full_sentence = sentence_1 + " " + sentence_2
print("38.", full_sentence)
print("----------------")

num = 10
if num % 2 == 0:
    print("39. Число парне")
elif num % 2 != 0:
    print("39. Число непарне" )
if num % 5 == 0:
    print("39. Число кратне 5")
print("----------------")

num = 9876
individual_digits = num//1000%10, num//100%10, num//10%10, num//1%10
print("40.", *individual_digits)
print("----------------")

n = 4
factorial = n * (n - 1) * (n-2) * (n-3)
print("41.", factorial)
print("----------------")

import random
a = random.randint(1, 100)
b = random.randint(1, 100)
print("42.")
if a > b:
    print("a", a, ">", "b" , b)
elif b > a:
    print("b", b, ">", "a", a)
else:
    print("a", a, "=", "b", b)
print("----------------")

text = "Львів - це Україна"
length = len(sentence)
space_count =  sum(1 for char in text if char == ' ')
print("43.", length, space_count)
print("----------------")

num = 3661
hours = num // 3600
minutes = (num % 3600) // 60
seconds = num % 60
print("44.", hours, "год", minutes, "хв", seconds, "сек")
print("----------------")

num = int(input("Введіть число: "))
if 10 <= num <= 99:
    print("45. Число двоцифрове")
else:
    print("45. Число не є двоцифрове")
print("----------------")

price = 1200
final_price = price * 0.2
final_final_price = price + final_price
print("46.", final_final_price)
print("----------------")

sentence_1 = "Qwerty"
sentence_2 = "ytrewQ"
sentence_1 = sentence_1.lower().replace(" ", "")
sentence_2 = sentence_2.lower().replace(" ", "")
if sorted(sentence_1) == sorted(sentence_2):
    print("47. Анаграми")
else:
    print("47. Не анаграми")
print("----------------")

a = 10
b = 5
c = 2
arithmetic = (a + b + c) / 3
print("48.", round(arithmetic, 2))
print("----------------")

text = "Python"
word = text[0], text[-1]
print("49.", word)
print("----------------")

a = 1452
b = 3256
c = 1500
if a>=b and a>=c:
    print("50. Максимальне число =", a)
elif b>=a and b>=c:
    print("50. Максимальне число =", b)
else:
    print("50. Максимальне число =", c)
print("----------------")