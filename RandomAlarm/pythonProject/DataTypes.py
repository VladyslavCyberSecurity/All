#1
from sympy.physics.units import joule

x = 10
print(type(x))

#2
pi = 3.14
print(type(pi))

#3
a = 'Hello, '
b = 'World!'
message = a + b

#4
a = 5
b = 3
aIsBigger = a > b
print(aIsBigger)

#5
a = '18'
b = int(a) + 3

#6
a = None
print(a)
print(type(a))

#7
z = 2 + 3j
print(type(z))
print(z.real)
print(z.imag)

#8
a = True
b = False
print(type(a))  # <class 'bool'>
print(1 > 2)    # False

#9
name = "Vladyslav"
text = 'Python is fun'
multi_line = """Це
багаторядковий
текст"""
print(type(name))  # <class 'str'>
print(name[0])   # 'V'
print(name[0:6]) # 'Vladys'

#10
nums = [1, 2, 3, 4]
nums.append(5)
nums[0] = 10
print(nums)  # [10, 2, 3, 4, 5]

#11
t = (1, 2, 3)
# t[0] = 10  -> Error

#12
r = range(0, 10, 2)  # 0,2,4,6,8
print(list(r))

#13
s = {1, 2, 3, 3}
print(s)  # {1, 2, 3}
s.add(4)
print(s)  # {1, 2, 3, 4}

#14
person = {"name": "Vlad", "age": 20}
print(person["name"])  # Vlad
person["age"] = 21
person["city"] = "Lviv"
print(person)  # {'name': 'Vlad', 'age': 21, 'city': 'Lviv'}

#15
x = None
print(type(x))  # <class 'NoneType'>

#16
x = 10      # int
y = float(x)  # перетворення в float
z = str(x)    # перетворення в str
b = bool(0)   # False
c = bool(5)   # True

#17
n = 3
a = n ** 2
b = n ** 3
print(a, b)

#18
a = 3.5
b = 7.2
c =(a+b)/2
print(c)

#19
z = 4 + 5j
print(z.real)
print(z.imag)

#20
x = -3
print(x > 0)

#21
s = "Python"
print(s[0:3])
print(s[4:6])

#22
nums = [1,2,3]
nums.append(100)
print(nums)

#23
tpl = (10,20,30,40,50)
middle_index = len(tpl) // 2
print(tpl[middle_index])

#24
r = range(5, 20, 3)
print(list(r))

#25
nums = [1,2,2,3,3,3]
unique_nums = set(nums)
print(unique_nums)

#26
name = "Vladyslav"
age = 20
print(age)

#27
x = None
if x in None:
    print("Змінна пуста")