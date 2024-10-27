total_grades = 0 
grade_count = 0
while True: 
    grade = float(input('Type your grade: '))
    total_grades += grade 
    grade_count += 1 
    more_grades = input('Do you want to type another grade? ')
    if more_grades != 'yes':
        break
if grade_count > 0:
    average = total_grades / grade_count
    print ('Your average grade is', average)
else:
    print ('No grades were insterted')