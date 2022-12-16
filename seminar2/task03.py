# Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.
def string (msg):
    string = str(input(msg))
    return string

string1 = string("Enter string1 ")
string2 = string("Enter string2 ")

def count(string1, sytring2):
    string1_list = []
    count=0
    for char in string1:
        string1_list.append(char)
    string1_set = set(string1_list)
    for item1 in string1_set:
        for item2 in string2:
            if item1 == item2:
                count+=1
    return count

c = count(string1, string2)

print(c)