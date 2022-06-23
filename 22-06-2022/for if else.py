student_name = 'gowri'

marks = {'asha': 90, 'gowri': 55, 'tharun': 77}

for student in marks:
    if student == student_name:
        print(marks[student])
        break
else:
    print('No entry with that name found.')