grade_1 = float(input('What is the first grade?'))
grade_2 = float(input('What is the second grade?'))
grade_3 = float(input('What is the third grade?'))

if grade_1 > grade_2 and grade_1 > grade_3:
    print('The highest grade is', grade_1)
elif grade_2 > grade_1 and grade_2 > grade_3:
    print('The highest grade is', grade_2)
else:
    print('The highest grade is', grade_3)
    

