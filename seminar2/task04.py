# Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.
def string (msg):
    string = str(input(msg))
    return string

string1 = string("Enter string1 ")
string2 = string("Enter string2 ")

print(string1.count(string2))
count = 0
for i in range(len(string1)-len(string2)+1):
    if string1[i:i+len(string2)] == string2:
        count+=1
print(count)









#1
#     n = int(input())
# num = 1
# print(num, end = " ")
# for i in range(1,n):
#     num*=-3
#     print(num, end = " ")

#3
# print (one_str.count (two_str))
# one_str[i:i+len(two_str)] == two_str
# one = input()
# two = input()
# # count = 0
# # for i in range(len(one)-len(two)+1):
# #     if one[i:i+len(two)] == two:
# #         count += 1
# # print(count)
# print(one.count(two))
