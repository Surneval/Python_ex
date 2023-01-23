import input as inp
import output as out


def button():
    action_flag = 0
    while action_flag != 5:
        try:
            action_flag = int(input(
                "If you want to add a record enter '1'.\n To look at phonebook - '2'.\n To sort - '3'.\n List of first and second names - '4'.\n To leave menu = '5'\n"))
        except (ValueError, TypeError):
            print('Mistake. Type 1, 2 or 3')
        if action_flag == 1:
            data_item = inp.record_file()
        elif action_flag == 2:
            out.print_as_is()
        elif action_flag == 3:
            out.sorting()
        elif action_flag == 4:
            out.only_name_surname()
        elif action_flag == 5:
            break
        else:
            print('Type 1, 2, 3, 4 to choose an option. Tyoe 5 to exit')
