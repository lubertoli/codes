# A program that prints the average and the names of the students who scored above average
def read_file():
    # reads the file and splits the content into a list of lines 
    # return the list of lines
    filename = 'marks.txt'
    file_mode = 'r'
    infile = open(filename,file_mode)
    content = infile.read()
    list_of_lines = content.splitlines()
    return list_of_lines
def find_average(lines):
    # finds the average of the students' marks
    # lines is a list of strings made up of name,mark
    # returns the average mark
    total = 0
    for string in lines:
        name,mark = string.split(',')
        total = total + int(mark)
    average = total//len(lines)
    return average
def find_names(lines,average):
    # find student names whose marks are above average
    # lines is bound to a list strings. Each string holds the name and mark of the student separated by a comma
    # average is bound to the average marks of the students
    # returns a list of names of students whose marks are above average
    above_average = []
    for string in lines:
        name,mark = string.split(',')
        if int(mark) > average:
            above_average.append(name)
    return above_average        
def display_results(average,names):
    # displays the average mark and the names of students who scored above average
    # average is bound to the average score
    # names is a list of names of students whose marks are above average
    print('The average mark is : ', average)
    print('Students whose marks are above average are :')
    for name in names:
        print(name)
    

def main():
    lines = read_file()
    average = find_average(lines)
    above_average = find_names(lines,average)
    display_results(average,above_average)
main()