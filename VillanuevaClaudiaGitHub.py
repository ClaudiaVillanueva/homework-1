# Claudia Villanueva Robles Term Project


def load_data(file_name):
    data = []
    #Open file and read each line
    with open(file_name, 'r') as f:
        for line in f.read().split('\n')[1:]:
            if not line:
                continue
            #Parse line and extract each field
            student = line.split('\t')
            if len(student) != 6:
                print('Invalid input file, missing student details')
                return None
            #Save student record in list
            data.append({'id': student[0],
                         'last': student[1],
                         'first': student[2],
                         'grad_year': student[3],
                         'grad_term': student[4],
                         'degree': student[5]})
    return data

def get_command():
    user_input = input('\nEnter your query: ').lower()
    command = user_input.split(' ')

    #Parse user input
    if len(command) == 1:
        if command[0] == 'all':
            return command
        elif command[0] == 'help':
            return command
    elif len(command) == 2:
        if command[0] == 'graduating':
            if command[1].isnumeric():
                return command
        elif command[0] == 'summary':
            if command[1].isnumeric():
                return command
        if command[0] == 'lastname':
            return command

    return None

def print_all_students(students):
    if not len(students):
        print('No records found')
        return

    print_header()
    #Print all student records
    for student in students:
        print(f"{student['id']}\t{student['first']}\t{student['last']}"
              f"\t{student['grad_year']}\t{student['grad_term']}"
              f"\t{student['degree']}")

def print_lastname_prefix(students, last_name_prefix):
    if not len(students):
        print('No records found')
        return

    print_header()
    #Print students with lastname prefix
    for student in students:
        if student['last'].lower().startswith(last_name_prefix.lower()):
            print(f"{student['id']}\t{student['first']}\t{student['last']}"
                  f"\t{student['grad_year']}\t{student['grad_term']}"
                  f"\t{student['degree']}")

def print_graduating(students, year):
    if not len(students):
        print('No records found')
        return

    print_header()
    #Print Student Graduating on a given year
    for student in students:
        if student['grad_year'] == year:
            print(f"{student['id']}\t{student['first']}\t{student['last']}"
                  f"\t{student['grad_year']}\t{student['grad_term']}"
                  f"\t{student['degree']}")

def print_summary(students, year):
    if not len(students):
        print('No records found')
        return

    programs = {}
    total = 0
    #Calculate student stats
    for student in students:
        if int(student['grad_year']) >= year:
            if not student['degree'] in programs:
                programs[student['degree']] = 0
            programs[student['degree']] += 1
            total += 1
    print('DEGREE\tSTUDENTS\tPERCENTAGE')
    #Print Summary
    for program in programs:
        students_in_program = programs[program]
        print(f'{program}\t{students_in_program}\t{(students_in_program * 100) / total: .2f}')


def print_header():
    print('\nID\tFIRST\tLAST\tGRAD_YEAR\tGRAD_TERM\tDEGREE')

def print_help():
    print('The following query types are supported:\n')
    print('all - Print all students')
    print('lastname [prefix] - Print students whose lastname starts with [prefix]')
    print('graduating [year] - Print students graduating on [year]')
    print('summary [year] - Print a summary of programs, student count and percentage '
          'graduating on or after [year]')
    print('help - Print this help')

def main():
    students = load_data("Students.txt")
    if not students:
        print('Invalid data or empty file provided')
        return -1

    #Start and infinite loop to acept queries and print results
    while True:
        command = get_command()
        if not command:
            print('Invalid query, use \'help\' to get the list of valid queries')
            continue

        if command[0] == 'all':
            print_all_students(students)
        elif command[0] == 'lastname':
            print_lastname_prefix(students, command[1])
        elif command[0] == 'graduating':
            print_graduating(students, command[1])
        elif command[0] == 'summary':
            print_summary(students, int(command[1]))
        elif command[0] == 'help':
            print_help()

main()