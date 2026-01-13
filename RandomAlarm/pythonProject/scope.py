#1
def square(num):
    return num**2
print(square(2))

#2
count = 2
def greet():
    global count
    count += 1
    print(count)
greet()

#3
def qwerty():
    x = 1
    def ytrewq():
        nonlocal x
        x += 1
        print(x)
    ytrewq()
    print(x)
qwerty()

#4
scope = 5
def arr():
    scope = 8
arr()
print(scope)

#5
for i in range(3):
    temp = i * 2
    print("В циклі: ",temp)

print("Поза циклом", temp)

#6
number = 5
def number():
    number = 5
    print("Function")

print("Global")

#7
PI = 3.14
def function():
    print(PI)
function()

#8
number = 2
def arr():
    print(number)
    number = 3
arr()

#9
def function():
    x = 1
    def fun():
        nonlocal x
        x = 10
        print(x)
    fun()
    print(x)
function()

#10
len = 5
print(len("Hello"))