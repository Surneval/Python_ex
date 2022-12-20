# working with files
# colors = ['red', 'green', 'blue3']
# data = open('file.txt', 'a')
# data.writelines(colors) #без разделителей
# data.write("\nLINE 12\n")
# data.write("LINE 33\n")
# data.close()

# with open("file.txt", "a") as data:
#     data.write("line 11\n")
#     data.write("line 21\n")
#     #data close appears automatically
# exit() #not to process further code

# path = "file.txt"
# data = open(path, "r")
# for line in data:
#     print(line)
# data.close()
# exit()

# import hello as h

# print(h.f(1))

# def new_string(symbol, count = 4):
#     return symbol * count
# print(new_string("!", 5))
# print(new_string("!"))

# def concatenetio (*params):
#     res: str = "" #type is fixed
#     #res: int = 0
#     for item in params:
#         res += item
#     return res

# print(concatenetio("a", "s", "d", "w"))
# print(concatenetio("a", "1"))

# def fib(n):
#     if n in[1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# list = []
# for e in range(1,10):
#     list.append(fib(e))
# print(list)

# tuple:
a = (3, 1, 2, 4)
# print(a)
# print(a[0])
# print(a[-2])

# for item in a:
#     print(item)

# #elements of tuple can be used in any way(the fitsr, the third etc)
# # **unpacking a tuple

# t = tuple(["red", "green", "blue"]) #making a tuple from list
# red, green, blue = t #making tuple members as independent values
# print("r:{} g: {} b:{}".format(red, green, blue))

# Dictionary
# dictionary = {}
# # \ - чтобы не пистаь все в 1 строку
# dictionary = \
#     {
#         "up": "1",
#         "left": "2",
#         "right": "3",
#         "down": "4"
#     }
# print(dictionary)
# print(dictionary["up"])

# for k in dictionary.keys():
#     print(k)

# for v, k in dictionary.items():
#     print(f"{k}: {v}")

###set - множества
# colors = {"red", "green", "blue"}
# print(type(colors))
# colors.add("red")
# print(colors)
# colors.add("gray")
# print(colors)
# colors.remove("red")
# print(colors)
# colors.discard("greon")
# print(colors)
# colors.clear()
# print(colors)

# a = {1, 2, 3, 4, 5}
# b = {3, 5, 7, 8}
# c = a.copy()
# print(c)
# u = a.union(b)
# print(u)
# i = a.intersection(b)
# print(i)
# d1 = a.difference(b)
# print(d1)
# d2 = b.difference(a)
# print(d2)
# q = a\
#     .union(b)\
#     .difference(a.intersection(b))
# print(q)
# s = frozenset(a)

list1 = [1, 2, 3, 4, 5]
list2 = list1
# list1[0] = 123
# list2[1] =345
# for e in list1:
#     print(e)
# print()

# for e in list2:
#     print(e)

#print(len(list1))
list1.insert(1, 22)
print(list1)
# print(list1.pop(2))
# print(list1)
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)