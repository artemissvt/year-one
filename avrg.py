total_grades = 0
grade_count = 0

while True:
    grade = float(input("Enter a grade: "))
    
    total_grades += grade
    grade_count += 1
    
    more_grades = input("Do you want to enter another grade? (yes/no): ")
    if more_grades != "yes":
        break
if grade_count > 0:
    average = total_grades / grade_count
    print("The average of the grades is:", average)
else:
    print("No grades were entered.")

