#Take user input
quiz_1 = float(input('Enter marks for quiz 1 >'))
quiz_2 = float(input('Enter marks for quiz 2 >'))

#print outputs according to compound statements
if quiz_1 >= 80 and quiz_2 >= 80:
    print('Level 3')
elif quiz_1 >= 50 and quiz_2 >= 50:
    print('Level 2')
elif quiz_1 < 50:
    if quiz_2 >= 50:
        print('Redo quiz 1')
    else:
        print('Level 1')
elif quiz_2 < 50:
    if quiz_1 >= 50:
        print('Redo quiz 2')
    else:
        print('Level 1')
        
