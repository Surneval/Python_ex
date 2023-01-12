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

with open("numbers.txt", mode='r+', encoding="utf-8") as data:
    numbers  = data.readlines()
print(numbers)