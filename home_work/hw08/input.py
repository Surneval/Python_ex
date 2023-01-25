# getting data from user

# new student add manually
school = {'Nadia Trusova': {'biology': [5, 4], 'chemistry': [
    5]}, 'Bill Gates': {'biology': [4, 5], 'chemistry': [3]}}
subject_list = ['biology', 'chemistry']


# add new student


def add_student(school, subj):
    new_student = input(
        'Enter First Name, Second Name. Use "space" as separator > ')
    school[new_student] = {}
    for item in subj:
        school[new_student][item] = []
    return school

# add new subject


def add_subject(school, subj):
    new_subject = input(
        'Enter new subject_name. Use "space" as separator if needed > ')
    subj.append(new_subject)
    for key in school:
        school[key][new_subject] = []
    return school

# add new mark


def add_marks(school):
    # for viewing all the students
    for key in school:
        print(key)
    student = input("Enter student First and Second Name > ")
    
    # for viewing list of all subjects
    subj_l = subjects_read(school=school)
    for item in subj_l:
        print(item)

    subject = input("Enter subject > ")
    try:
        new_mark = int(input("Enter new mark (from 1 to 5) > "))
    except (ValueError, TypeError):
        print("Error. Type a number > ")
    if new_mark < 1 or new_mark > 5:
        try:
            new_mark = int(input("Enter new mark (from 1 to 5) > "))
        except (ValueError, TypeError):
            print("Error. Type a number > ")
    for key in school:
        if key == student:
            for sub in school[student]:
                if sub == subject:
                    school[student][subject].append(new_mark)
    return school

# write in file

def write_file(school):
    file = open(
        r'C:\Users\nadez\Desktop\Python\home_work\hw08\school.txt', mode='w')
    for stud in school:
        file.write(f'{stud}_')
        for subj in school[stud]:
            line = '{}:{}*'.format(subj, school[stud][subj])
            print(line)
            file.write(line)
        file.write(f'\n')
    file.close()

# read fron file
def read_file():
    with open(r'C:\Users\nadez\Desktop\Python\home_work\hw08\school.txt', mode='r') as file:
        data = file.read().splitlines()
    names = []
    school_base = {}

    for item in data:
        data_l = item.split('_')
        stud_name = data_l[0] # determine  stident name
        school_base[stud_name] = {} #add empty element (only name) to a school_base dictionary
        names.append(stud_name) # add name to the list of names
        subj_m = data_l[1].split('*') #list of subjects and marks for certain student. Every elem is "sub:[marks]"
        subject_marks = {}
        for ind in range(len(subj_m)-1): #iterate: get each pair "sub:[marks]"
            work_list = subj_m[ind].split(':') # separate list [subject, [marks]]
            work_sub = work_list[0] #get subject name
            work_mark = [] # empty marks list
            for char in work_list[1]: #lookong through the second part [mark1, mark2, ...]
                if char.isdigit(): #searching for digits
                    work_mark.append(int(char)) #if digit is found - append to list of marks
            subject_marks[work_sub] = work_mark
        school_base[stud_name] = subject_marks
    return school_base

def subjects_read(school):
    subjects_read = []
    for k, v in school.items():
        for key in school[k]:
            subjects_read.append(key)
        break
    return subjects_read

   
def write_file1():
    with open(r'C:\Users\nadez\Desktop\Python\home_work\hw08\school1.txt', mode='w+') as file:
        file.write(school)


def random_student(school, subj):
    # adding 100 students
    names = ['Anna', 'Bill', 'George', 'Ken', 'Luk', 'Bron',
             'Anastasia', 'Ketty', 'Maria', 'Alise', 'Robert']

    surnames = ['Brown', 'Green', 'Red', 'Blue', 'Dark', 'White',
                'Winter', 'Snow', 'Summer', 'Spring', 'Night', 'Dorwood']

    import random
    count = 0
    while count < 101:
        new_student = str(random.choice(names) + ' ' + random.choice(surnames))
        school[new_student] = {}
        for item in subj:
            school[new_student][item] = []
        count += 1
    return school


def random_subjects(school, subj):
    import random
    random_subjects = ['maths', 'russian', 'english', 'french',
                       'german', 'cs', 'drowing', 'literature', 'phisics', 'sport', 'culture']
    try:
        quantity = int(input("Enter a quantity of subjects to generate > "))
    except (ValueError, TypeError):
        print("Error. Type a number > ")
    count = 0
    while count < quantity + 1:
        new_subject = random.choice(random_subjects)
        subj.append(new_subject)
        for key in school:
            school[key][new_subject] = []
        count += 1
    return school

def random_marks(school):
    import random
    try:
        quantity = int(input("Enter a quantity of marks to generate > "))
    except (ValueError, TypeError):
        print("Error. Type a number > ")
    count = 0
    while count < quantity + 1:
        for key in school:
            for sub in school[key]:
                mark = random.randint(1, 5)
                school[key][sub].append(mark)
        count += 1
    return school

# testing_module!!!
# count = 0
# while count != 3:
#     school = add_student(school=school,subj = subject_list)
#     school = add_subject(school=school, subj=subject_list)
#     count += 1

# school = add_marks(school=school)

# print(school)
# write_file()
# school1 = read_file()
# print(school==school1)
# print(school1)