# getting data from user

# new student add
school = {}

def add_student(school):
    new_student = input(
        'Enter First Name, Second Name. Use "space" as separator > ')
    school[new_student] = {}
    # school.update({new_student:{None}})
    return school

# add new subject

def add_subject(school):
    new_subject = input(
        'Enter new subject_name. Use "space" as separator if needed > ')
    for key in school:
        school[key][new_subject] = []
    return school

#add new mark
def add_marks(school):
    student = input("Enter student First and Second Name > ")
    subject = input("Enter subject > ")
    try:
        new_mark = int(input("Enter new mark (from 1 to 5) > "))
    except (ValueError, TypeError):
        print("Error. Type a number")
    if new_mark < 1 or new_mark > 5:
        try:
            new_mark = int(input("Enter new mark (from 1 to 5) > "))
        except (ValueError, TypeError):
            print("Error. Type a number")
    for key in school:
        if key == student:
            for key in school[student]:
                if key == subject:
                    school[student][subject].append(new_mark)
    return school


count = 0
while count != 3:
    school = add_student(school=school)
    school = add_subject(school=school)
    school = add_marks(school=school)
    count += 1
print(school)
with 
