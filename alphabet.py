#write a function that reads a file and it return a list with the words that start with a particular letter

def alphabetical_collection(start_letter):
    filename = 'words.txt'
    file_mode = 'r'
    infile = open(filename,file_mode)
    content = infile.read()
    infile.close()
    alist = content.splitlines90
    matches = []
    for word in alist:
        if word[0] == start_letter:
            matches.append(word)
    return matches

def main():
    start_letter = input('Enter first letter >')
    result = alphabetical_collection(start_letter)
    print(result)
main()    