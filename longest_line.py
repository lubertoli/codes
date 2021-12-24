filename = 'random_file.txt'
file_mode = 'r'
infile = open(filename,file_mode)
content = infile.read()
infile.close()
#print(repr(content))
list_of_lines = content.splitlines()
#print(list_of_lines)
longest_line = list_of_lines[0]
for line in list_of_lines:
    if len(line) > len(longest_line):
        longest_line = line
max_length = len(longest_line)
print('The longest line was ' + str(max_length) + ' characters long.')