#data output
import input as i

#school = i.school

def print_names(school):
    for student in school:
        student = student.split()
        print('%-9s %-9s' % (student[0], student[1]))

def mark_student(school):
    for student in school:
        print(student) #tips - whom to choose
    person = input("Enter student name to look at marks > ")
    for student in school:
        if student == person:
            for k,v in school[person].items():
                print('{}: {}\n'.format(k, v))
       
def read_file():
    with open(r'C:\Users\nadez\Desktop\Python\home_work\hw08\school.txt', mode='r') as file:
            data = file.read().splitlines()
    return data

def student_GPA_1subject(school):
    # for viewing all the students
    for key in school:
        print(key)
    student = input("Enter student First and Second Name > ")
    
    # for viewing list of all subjects
    subj_l = i.subjects_read(school=school)
    for item in subj_l:
        print(item)
    
    subject = input("Enter subject > ")
    gpa = 0
    for key in school:
        if key == student:
            for sub in school[student]:
                if sub == subject:
                    for item in school[student][subject]:
                        gpa += item
                    gpa /= len(school[student][subject])  
    print(f'{student} GPA for {subject} equals {round(gpa, 2)}')  

def gpa_school_subject(school):
    
    # for viewing list of all subjects
    subj_l = i.subjects_read(school=school)
    for item in subj_l:
        print(item)

    subject = input("Enter subject > ")
    gpa = 0
    count = 0
    for key in school:
        for sub in school[key]:
            if sub == subject:
                for item in school[key][subject]:
                    gpa += item
                    count += 1
    gpa /= count
    print(f'Average school GPA for {subject} equals {round(gpa, 2)}')

# golden medal
def golden_medai(school):
    count = 0
    flag = True
    for stud in school:
        for sub in school[stud]:
                for item in school[stud][sub]:
                    flag = flag and item >= 4
        if flag == True:
            count += 1
    print(f'{count} students are going to get golden medal')
