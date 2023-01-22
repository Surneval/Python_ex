# data request from user
def new_index():
    with open(r'C:\Users\nadez\Desktop\Python\home_work\hw07\telephone.csv', 'r') as file:
        data = file.read().splitlines()
        index = len(data) + 1
    return index

def data_request():
    data_item = input('Enter First Name, Second Name, phone number, comment. Use ";" as separator')
    return data_item

# write in file
def record_file(item):
    id = new_index()
    with open(r'C:\Users\nadez\Desktop\Python\home_work\hw07\telephone.csv', 'a') as file:
            file.write('{}; {}\n'
                        .format(id, data_item))