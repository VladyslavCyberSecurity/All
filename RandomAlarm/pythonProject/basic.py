#1
a = 2
b = "word"
c = None
d = 2.25
e = 2 + 2j
my_list = [a, b ,c]
my_tuple = (a, b, c)
my_dict = {a, b ,c}
print(type(my_list))

#2
a = 10
if a % 2 == 0 and a >=0:
    print("Парне")
else:
    print("Не парне")

#3
my_list = [1, 2, 3]
my_list.append(100)      # додаємо
if 1 in my_list:         # видаляємо 0, якщо він є
    my_list.remove(1)
print(my_list)

#4
sum1 = 0
for i in range(1, 100):
    sum1 += i
print(sum1)

#5
def function():
    num = [1,2,3,4,5]
    return sum(num)/2
print(function())

#6
a = 5
def qwe():
    global a
    a = 10
    print(a)
qwe()
print(a)

#7
n = 37
print(bin(n))
print(hex(n))

#8
num = 37          # приклад
mask = 1 << 2     # 3-й біт (рахуємо з 0)
if num & mask:
    print("3-й біт встановлений")
else:
    print("3-й біт не встановлений")

#9
for A in [False, True]:
    for B in [False, True]:
        for C in [False, True]:
            print(A, B, C, (A and not B) or C)

#10
a = int(input("Перше число: "))
b = int(input("Друге число: "))
op = input("Операція (+ - * / // % **): ")
if op == '+': print(a+b)
elif op == '-': print(a-b)
elif op == '*': print(a*b)
elif op == '/': print(a/b)
elif op == '//': print(a//b)
elif op == '%': print(a%b)
elif op == '**': print(a**b)
else: print("Невідома операція")