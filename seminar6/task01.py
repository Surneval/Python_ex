#list comprehension
import random
a = [random.randint(1,10) for i in range(1,10)]
print(a)
#with a condition
a = [i for i in range(1,10) if i%2==0]
print(a)

#enumerate
a = [2, 4, 6, 8]
for index,val in enumerate(a):
    if val>5:
        a[index] = 0 #берет соответствующий индекс
print(a)
#zip объединение последовательностей в одну
a = [1,2,3,4,5,6]
months = ['june', 'july', 'august', 'september', 'october', 'november']
dictionary = {1:'ddd', 2:'112'}
result = list(zip(a, months, dictionary))
print(result[1][1])#результат от 2

#lambda
def sum(a,b):
    return a+b
print(sum(1,2))

sum = lambda a,b, *args: a+b if a <5 else 0
print(sum(1,6))
print(sum(1,2,3,4))
def sum(a,b, *args):
    print(type(args))
    return a+b
print(sum(1,2,3,4,5,6))

def sum(a,b, *args):
    for i in args:
        print(i)
    return a+b

print(sum(1,2,3,4,5,6))

#map - to apply some function to every element of the list

a = [1,2,3,4,5]
print(a)
a = list(map(lambda x: x*x, a))
print(a)

#filter
a  = [1,2,3,4,5,6,7,8]
def sorting(x):
    if x%2 ==0:
        return True

res = list(filter(sorting,a))
res = list(filter((lambda x: not x % 2), a))
print(res)
#sorted
a = [(2,4,6), (4,4,6), (1,2,3)]
#sort by 3rd element, if 3rd is the same, sort by second element
res = sorted(a, key=lambda x: (x[2], x[1], x[0]), reverse=True)#key - ключ сортировки
print(res)