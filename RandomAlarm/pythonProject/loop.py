for i in range(2, 51):
    while i % 2 == 0:
        print(i, end=" ")
#1
n = int(input("Enter n: "))
i = 1
while i <= n:           # loop while condition is true
    print(i, end=" ")
    i += 1
#2
total = 0
for x in range(1, 11):  # from 1 to 10 inclusive
    total += x ** 2
print()
print("Sum of squares =", total)
#3
fruits = ['banana', 'apple', 'greple']
for fruit in fruits:    # for-each element in list
    print(fruit.capitalize())
#4
while True:
    number = int(input("Enter positive number: "))
    if number > 0:
        print("Thanks!")
        break
    else:
        print("Try again")  # loop continues until condition met
#5
n = 50
i = 2
while i <= n:
    print(i, end=" ")
    i += 2
#6
n = int(input("Enter N: "))
fact = 1
for i in range(1, n + 1):     # loop from 1 to N inclusive
    fact *= i                # multiply fact by i each step
print(f"Factorial of {n} is {fact}")
#7
words = ['pad', 'worker', 'study', 'barber', 'qwerty']
count = 0
for w in words:
    if len(w) > 5:
        count += 1
print()
#8
while True:                                   # infinite loop
    password = input("Enter password: ")
    if password == "secret":                  # check condition
        print("Access granted!")
        break                                 # exit loop
    else:
        print("Wrong password, try again.")
#9
sentences = [
    "I love playing guitar",
    "Python is powerful",
    "Practice makes perfect"
]
vowels = "aeiou"
total_vowels = 0
for s in sentences:
    for ch in s.lower():
        if ch in vowels:
            total_vowels += 1
print(f"Total vowels: {total_vowels}")
#10
while True:
    try:
        num = int(input("Enter an integer 1-100: "))
        if 1<=num<=100:
            print(f"Valid number: {num}")
            break
        else:
            print("Number out of range. Try again.")
    except ValueError:
        print("That`s not an integer. Try again")
#11
n = int(input("Enter n: "))
for i in range(1, 11):
    result = n * i
    print(f"{n} x {i} = {result}")
#12
total = 0
while True:
    num = int(input("Enter N: "))
    if num == 0:
        print(total)
        break
    else:
        total += num
#13
sentence = ["Pid provodom Stepana Bandery"]
vowels = "aeyuio"
total_vowels = 0
for s in sentence:
    for ch in s.lower():
        if ch in vowels:
            total_vowels += 1
print(f"Total vowels: {total_vowels}")
#14
N = int(input("Enter N: "))
even_nums = 0
odd_nums = 0
for n in range(1, N+1):
    if n % 2 == 0:
        even_nums += 1
    else:
        odd_nums +=1
print(f"Even: {even_nums}, Odd: {odd_nums}")
#15
text = input("Enter a string: ")
reversed_text = ""

for char in text:
    reversed_text = char + reversed_text  # додаємо символ попереду

print("Reversed string:", reversed_text)
#16
max_num = None
while True:
    value = input("Enter a number or stop: ")
    if value == 'stop':
        break
    num = int(value)
    if max_num is None or num > max_num:
        max_num = num
print("max num:", max_num)
#17
N = int(input("Enter N: "))
squares = []
for i in range(1, N+1):
    squares.append(i ** 2)
print("Squares: ", squares)
#18
h = int(input("Enter height: "))
for i in range(1, h + 1):
    print("*" * i)
#19
cities = ["Kyiv", "Lviv", "Odessa", "Kharkiv", "Dnipro"]
search = input("Enter city to search: ")
found = False
for city in cities:
    if city.lower() == search.lower():
        found = True
        break
if found:
    print("Found")
else:
    print("Not found")
#20
correct_password = "Bandera1909"
while True:
    pwd = input("Enter password: ")
    if pwd == correct_password:
        print("Access granted")
        break
    else:
        print("Wrong password")
