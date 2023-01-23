# read current version of thr database fron the existing csv file

def read_file():
    with open(r'C:\Users\nadez\Desktop\Python\home_work\hw07\telephone.csv', mode='r') as file:
            data = file.read().splitlines()
    return data

def print_as_is():
    data = read_file()
    data_sub = [item.split() for item in data]
    for item in data_sub:
        print('%-3s %-6s %-9s %-6s %-6s' % (item[0], item[1], item[2], item[3], item[4]))

def sorting():
    data = read_file()
    data_sub = [item.split() for item in data]
    try:
        type_sort = int(input('Type "0" to sort by ID, "1" to sort by Second Name, "2" to sort by First Name'))
    except(ValueError, TypeError):
        print("Mistake. Try again: type 0, 1 or 2 to choose sorting mode")
    if type_sort == 0:
        data_sub = sorted(data_sub, key=lambda x: int(x[0]))
    elif type_sort == 1:
        data_sub = sorted(data_sub, key=lambda x: x[2])
    elif type_sort == 2:
        data_sub = sorted(data_sub, key=lambda x: x[1])
    else:
        print("Mistake. Try again: type 0, 1 or 2 to choose sorting mode")
           
    for item in data_sub:
        print('%-3s %-6s %-9s %-6s %-6s' % (item[0], item[1], item[2], item[3], item[4]))
        
def only_name_surname():
    data = read_file()
    data_sub = [item.split() for item in data]
    for item in data_sub:    
        print('%-9s %-9s' % (item[1], item[2]))
    



