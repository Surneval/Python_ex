#aninymous and lambda

# def f(x):
#     x**2

# print(type(f))
# g = f
# print(f(1))
# print(g(1))

# def f(x):
#     return x**2
# g = f

# print(type(f))
# print(type(g))
# print(f(2))
# print(g(4))

# def calc(x):
#     return x + 10

# #print(calc(10))

# def calc2(x):
#     return x * 10

# #print(calc(10))

# def math(op, x):
#     print (op(x))

# math(calc2, 10)
# math(calc, 10)

# def sum(x, y):
#     return x + y
# sum = lambda x, y: x + y+1

# def mult(x, y):
#     return x * y

# def calc(op, a, b):
#     print(op(a, b))
#     #return op(a, b)
# calc(lambda x, y: x + y, 3, 5)
# calc(mult, 2, 3)

#list comprehensions
# [exp for item in iterable]
# [exp for item in iterable (if conditional)]
#[exp <if conditional> for item in iterable (if conditional)]

# list1 = []

# for i in range(1, 10):
#     if i % 2 == 0:
#         list1.append(i)
# print(list1)

# def f(x):
#     return x ** 3

# list2 = [f(i) for i in range (1, 10) if i % 2 == 0]
# print(list2)

# with open(r"C:\Users\nadez\Desktop\Python\Lection3\numbers.txt", mode='r+', encoding="utf-8") as data:
#     numbers = data.read().splitlines()
#     list1 = [(int(i), int(i)**2) for i in numbers if int(i) % 2 == 0]
# print(list1)

# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()
# res = select(int, data)
# print(res)
# res = where(lambda x: not x % 2, res)
# res  = select(lambda x: (x, x**2), res)
# print(res)

#map function
# li = [x for x in range(1, 20)]
# li = list(map(lambda x: x + 10, li))
# print(li) 
# data = list(map(int, input('Enter a number > ').split()))
# print(data)
# data2 = map(int, input('Enter a number > ').split())
# for e in data2:
#     print(e)
# print('__')
# for e in data2:
#     print(e)

# ## filter you cant do it twice
# it takes some function and then check every iterable item and checking is it True
# if Yes, it returns the itrrable item

# data = [x for x in range(10)]
# res = list(filter(lambda x: not x % 2, data))

# print(res)

## zip function
# you are taking some lists and zip function returns tuples
#zip([1,2,3], ['a', 's', 'd'], ['z', 'x', 'c'])
#[(1,'a', 'z'), (2, 's', 'x'), (3, 'd', 'c')]
#you can't use it twice

# users = ['u1', 'u2', 'u3']
# ids = [3,5,7]
# salary = [100, 200]
# data = list(zip(users, ids, salary))
# print(data)

## enumerate function
# input - some data set, output - tuple (index, iterable element)
#you can't use it twice
#print(list(enumerate(['Moscow', 'Kazan', 'Paris'])))
#[(0, 'Moscow'), (1, 'Kazan'), (2, 'Paris')]

users = ['u1', 'u2', 'u3']

data = list(enumerate(users))
print(data)