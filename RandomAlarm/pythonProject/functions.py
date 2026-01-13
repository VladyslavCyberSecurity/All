#1
def hello_user(name):
    return f"Hello, {name}"
print(hello_user("Givno"))
print(hello_user("Asdfg"))
print(hello_user("Zxcvb"))

#2
def stats(numbers):
    total = sum(numbers)
    mid = total / len(numbers)
    return total, mid
print(stats([2, 3, 4]))

#3
def is_even(n):
    return n % 2 == 0
print(is_even(4))
print(is_even(16))
print(is_even(325))

#4
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
print(factorial(5))
print(factorial(12))

#5
numbers = [1,2,3,4,5,6]
even_nums = list(filter(lambda x: x % 2 == 0, numbers))
print(even_nums)

#6
def ConvertToCelsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius
def ConvertToFahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit
print(ConvertToCelsius(20))
print(ConvertToFahrenheit(20))

#7
def my_max(*args):
    return max(args)
print(my_max(1,2,3,4,5))

#8
def is_palindrome(text):
    clean = ''.join(ch.lower() for ch in text if ch.isalnum())  # без пробілів і регістру
    return clean == clean[::-1]

print(is_palindrome("Level"))          # True
print(is_palindrome("Python"))         # False

#9
def digit_sum(n):
    n = abs(int(n))
    return sum(int(d) for d in str(n))
print(digit_sum(12345))

#10
def multiplication_table(n, up_to=10):
    for i in range(1, up_to +1):
        print(f"{n} x {i} = {n * i}")
multiplication_table(3, 5)

#11
import math
from math import pi
def circle_area(r):
    circle = pi * (r ** 2)
    return circle
def rectangle_area(a, b):
    rectangle = a * b
    return rectangle

print(circle_area(2))
print(rectangle_area(2, 4))

#12
def is_multiple(x, y):
    if y == 0:              # перевірка на 0
        return False
    return x % y == 0       # True, якщо ділиться на y без залишку

print(is_multiple(6, 3))   # True
print(is_multiple(7, 3))   # False
print(is_multiple(5, 0))   # False

#13
def even_numbers(start, end):
    result = []
    for n in range(start, end + 1):
        if n % 2 == 0:
            result.append(n)
    return result
print(even_numbers(1, 10))

#14
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # перевіряємо дільники до √n
        if n % i == 0:
            return False
    return True

# Перевірка
print(is_prime(2))   # True
print(is_prime(3))   # True
print(is_prime(4))   # False
print(is_prime(17))  # True
print(is_prime(20))  # False

#15
def reverse_list(lst):
    return lst[::-1]
print(reverse_list([1,2,3,4]))

#16
def sort_words(sentence):
    sentence = sentence.lower()
    words = sentence.split()
    return sorted(words)
print(sort_words("I love Stepan Bandera"))

#17
def average(*args):
    if not args:
        return None
    return sum(args)//len(args)
print(average(2, 4, 6))

#18
def short_words(words, n):
    result = []
    for word in words:
        if len(word) <= n:
            result.append(word)
    return result
print(short_words(["uku", "qwert", "asdfg", "aka"], 4))

#19
def power (x, n=2):
    return x ** n
print(power(3))

#20
def count_vowels(text):
    count = 0
    vowels = "aeiou"
    text = text.lower()
    for char in text:
        if char in vowels:
            count +=1
    return int(count)
print(count_vowels("Stepan Bandera"))