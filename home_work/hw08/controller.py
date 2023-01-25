# control panel
import input as i
import output as out

def update_school():
    school = {}
    for k, v in i.school.items():
        school[k] = v
    return school

def update_subjects():
    subject_list = []
    for item in i.subject_list:
        subject_list.append(item)
    return subject_list

def button_click():

    school = update_school()
    subject_list = update_subjects()

    mode_flag = 0
    input_flag = 0
    while mode_flag != 5:
        try:
            mode_flag = int(input(
                "Type '1' to add data > \nType '2' to see the current version > \nType '3' to write data in file > \nType '4' to get data from file > \nType '5' to exit > "))
        except (ValueError, TypeError):
            print("Error. Type a number")
        if mode_flag == 1:
            try:
                input_flag = int(input(
                    "Type '1' to add new student > \nType '2' to add new subject > \nType '3' to add new mark > \nType '4' to randomly generate 100 students > \nType '5' to randomly generate subjects > \nType '6' to randomly add marks > "))
            except (ValueError, TypeError):
                print("Error. Type a number > ")
            if input_flag == 1:
                school = i.add_student(school=school, subj=subject_list)
            elif input_flag == 2:
                school = i.add_subject(school=school, subj=subject_list)
                subject_list = i.subjects_read(school=school)
            elif input_flag == 3:
                school = i.add_marks(school=school)
            elif input_flag == 4:
                school = i.random_student(school=school, subj=subject_list)
            elif input_flag == 5:
                school = i.random_subjects(school=school, subj=subject_list)
                subject_list = i.subjects_read(school=school)
            elif input_flag == 6:
                school = i.random_marks(school=school)
            else:
                print('Mistake. Type a number from "1" to "6" > ')
        elif mode_flag == 2:
            try:
                output_flag = int(input(
                    "Type '1' to look at students names > \nType '2' to look at certain student marks > \nType '3' to look at student' GPA for 1 subject > \nType '4' to look at average school GPA for 1 subject > \nType '5' to look at golden medals count > "))
            except (ValueError, TypeError):
                print("Error. Type a number")
            if output_flag == 1:
                out.print_names(school=school)
            elif output_flag == 2:
                out.mark_student(school=school)
            elif output_flag == 3:
                out.student_GPA_1subject(school=school)
            elif output_flag == 4:
                out.gpa_school_subject(school=school)
            elif output_flag == 5:
                out.golden_medai(school=school)
            else:
                print('Mistake. Type a number from "1" to "4" >')
        elif mode_flag == 3:
            i.write_file(school=school)
        elif mode_flag == 4:
            school = i.read_file()
            print(f"You got data from txt:\n{school}")
            subject_list = i.subjects_read(school=school)
        else:
            print('Mistake. Type a number from "1" to "5" >')
