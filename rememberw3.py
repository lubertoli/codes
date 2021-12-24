# Remember The Word Design
# Remember Version 3 - clear the screen,
#                    - conditional feedback,
#                    - identify and replace adjacent duplicate line groups with a for statement
#                    - Sw Quality Requirement
#                         - identify any literal in our program that occur more than once
#                         - bind that literal to an identifier
#                         - replace that literal with the identifier
#                    - random selection of 4 words from a list of words read from a file
#                    - random selection of answer from the 4 words
import time, os, random

# clear screen
clear_command = 'clear'
if os.name == 'nt':
    clear_command = 'cls'
os.system(clear_command)

# display header
header_border = '-' * 80
header_content = 'Remember the Word'
print(header_border)
print(header_content)
print(header_border)

# display instructions
filename = "intructions.txt"
file_mode = 'r'
infile = open(filename,file_mode)
content = infile.read() # read is a method call
infile.close()
print(content)

# prompt player to press enter
input("Press enter key to display the words.") # Ignore the return object from the input function

# clear screen
os.system(clear_command)
# display header
print(header_border)
print(header_content)
print(header_border) 

# display four words
#   - display word one at a time
#   - 1 sec pause before the word disappears and the next word appears
#   - words are chosen randomly from a list
#   - words start with different letters
filename = 'words.txt'
file_mode = 'r'
infile = open(filename, file_mode)
all_words = infile.read()
all_words_list = all_words.splitlines()
words = random.sample(all_words_list,4)

answer = random.choice(words)
start_letter = answer[0]

pause_time = 1
for word in words:
    print(word)
    time.sleep(pause_time)
    os.system(clear_command)
    # display header
    print(header_border)
    print(header_content)
    print(header_border)        
   
# prompt player to enter a word that starts with a particular letter
guess = input('What word starts with the letter '+start_letter+'?')
#   - answer is chosen randomly from the four words that are displayed
#   - use first letter of answer to prompt player
# evaluate answer and display feedback
if guess.lower() == answer.lower():
    #   - congratulations message is displayed if player answers correctl
    print('Congratulations,you are correct!')
    print('The answer was '+answer+'.')
else:
    #   - otherwise condolence message
    print('Sorry you entered '+guess+".")
    print('The answer was '+answer+'.')
# prompt player to play again

#    - program restarts if player chooses to play again
#    - otherwise program terminates
reply = input("Play again? y/n")
