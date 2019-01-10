import csv


filename = 'data.csv'
with open(filename, newline='') as f:
    reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
    subject_in_Semester = []
    seperator = [',,']
    semester = 0
    for row in reader:
        if row == seperator: # make a new list
            semester += 1
            # row.append(semester)
        elif row == ['Subject,Credits,Grade']: # make exception on first row
            continue
        else: # add all of subject in new list, identify by semester
            subject_in_Semester.append([semester,row])

def translate_grade_to_number(grade_char): # Get char return number
    if grade_char == 'A':
        grade_num = 4
    elif grade_char == 'B+':
        grade_num = 3.5
    elif grade_char == 'B':
        grade_num = 3
    elif grade_char == 'C+':
        grade_num = 2.5
    elif grade_char == 'C':
        grade_num = 2
    elif grade_char == 'D+':
        grade_num = 1.5
    elif grade_char == 'D':
        grade_num = 1
    elif grade_char == 'F':
        grade_num = 0
    else:
        grade_num = False
        print('Error value grade should be in char')
    return grade_num

def unpacklist(argv): # take list contain string, split into small item in list
    argv = argv.split(',')
    return argv


# Input
all_grade = []
#a = int(input('Which Semester you want to view? (answer 1 to '+ str(semester) + ') :'))
a = 2 # default to 2 for easy test
for i in subject_in_Semester:
    if i[0] == a:
        j = unpacklist(*i[1]) # Show only subject in correct semester
        all_grade.append(translate_grade_to_number(j[2]))
        print(j)
        print(all_grade)
