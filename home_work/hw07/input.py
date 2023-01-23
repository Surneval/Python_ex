# new index based in the previous entries
def new_index():
    with open(r'C:\Users\nadez\Desktop\Python\home_work\hw07\telephone.csv', 'r') as file:
        data = file.read().splitlines()
        index = len(data)
    return index

# data request from user
def data_request():
    data_item = input('Enter First Name, Second Name, phone number, comment. Use "space" as separator')
    return data_item

# write in file
def record_file():
    data_item = data_request()
    id = new_index()
    with open(r'C:\Users\nadez\Desktop\Python\home_work\hw07\telephone.csv', 'a') as file:
            file.write('{} {}\n'
                        .format(id, data_item))