# dictionary is a built-in data type 
# dictionary is made up of key:value pairs
# Keys are unique in a dictionary
# Keys are immutable - we cannot have a list as a key, we cannot have a dictionary as a key
# values can be of any type
grade_book = {'Fred':99, 'Barney':87, 'Wilma':93}
print(grade_book)

print('Using the item method in the dictionary class')
#for item in grade_book.items():
    #print(item[0],item[1])
for key,value in grade_book.items():
    print(key,value)
    
print('Using the keys method in the dictionary class')
for key in grade_book.keys():
    print(key, grade_book.get(key))
print('Using the values method in the dictionary class')
result = 0
for value in grade_book.values():
    result = result + value
average = result/len(grade_book)
print(average)