# print("Hello world!")
# a = 123
# b = 1.23
# print(a)
# print(b)
# value  = None
# value = 123
# print(value)
# print(type(a))
# s = 'rtg'
# print(type(s)) #type s
# print(a,b,s)
# print(a, " - ", b, " - ", s )
# print('{2} - {0} - {1}'.format(a,b,s))
# print(f'{a} - {b} - {s}')

# f = True
# print(f)

# list = ['1', '2', 'true']
# print(list)
# print("Enter a")
# a = float(input())
# print("Enter b")
# b = float(input())
# print(a,' + ', b, ' = ', a + b)
# print('{0} - {1}'.format(a,b))
# print(f'{a} - {b}')
# a = 2.234
# b = 8.123
# c = a+b
# d = a // b
# k = a % b
# n = round(a ** b, 4)
# print(c, d, k, n)
# a = 1 <= 3 and 5 > 2
# print(a)
# k = 1 < 3 < 5
# print(k)

# f = [1, 2, 3, 4]
# print(not 2 in f)

# is_odd = not f[0] % 2
# print(is_odd)
# print("enter l")
# l = int(input())
# print("Enter z)")
# z = int(input())
# if l > z:
#    print(l)
# else:
#   print(z)
# user_name = input("Enter name: ")
# if user_name == "Masha":
#     print("Hurrah, it's Masha!")
# elif user_name == "Mirina":
#     print("Oh I was waiting for you, Marina")
# elif user_name == "Ilnar":
#     print("Ilnar - top")
# else:
#     print('hello, ', user_name)

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //=10
#     print(original)
# else:
#     print("Stop, please")
# print(inverted)
# r = range(1, 10, 3)
# for i in "qwerty":
#     print(i)
# text = "съешь ещё этих мягких французских булок"
# print(text[0])
# print(text[1])
# print(text[len(text) - 1])
# print(text[-5])
# print(text[:])
# print(text[0:2])
# print(text[len(text)-2:])
# print(text[0:len(text):6])

# ran = range(1, 6)
# print(type(ran))
# numbers = list(ran)
# print(type(numbers))
# print(f' {len(numbers)} len')

# for i in numbers:
#     i *= 2
#     print(i)
# print(numbers)
# colors = ["red", "green", "blue"]

# for e in colors:
#     print(e)
# for e in colors:
#     print(e*2)
# colors.append("grey") #добавить в конец
# print(colors == ["red", "green", "blue", "grey"])
# colors.remove("red") #delete colors[0]
# print(colors)
# del colors[0]
# print(colors)

def f(x):
    if x ==1:
        return "integer"
    elif x ==2.3:
        return 23
    else:
        return
arg = 1
print(f(arg))
#print(type(f(arg)))