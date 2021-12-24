# Remember The Word Design
import time,os
# clear screen
clear_command = 'clear'
if os.name =='nt':
    clear_command = 'cls'
os.system(clear_command)
# display header
print("#" * len('Remember the Word'))
print("Remember The Word")
print("#" * len('Remember the Word'))
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
# display four words
#   - display word one at a time
#   - 1 sec pause before the word disappears and the next word appears
#   - words are chosen randomly from a list
#   - words start with different letters
words = ['orange','chair','sandwich','mouse']
for word in words:
    print(word)
    time.sleep(1)
    os.system(clear_command)
    # display header
    print("#" * 80)
    print("Remember The Word")
    print("#" * 80)    
    # prompt player to enter a word that starts with a particular letter
guess = input("What word starts with the letter m?")
#   - answer is chosen randomly from the four words that are displayed
#   - use first letter of answer to prompt player
# evaluate answer and display feedback
if guess == 'mouse':
    #   - congratulations message is displayed if player answers correctl
    print('Congratulations,you are correct!')
    print('The answer was mouse.')
else:
    #   - otherwise condolence message
    print('Sorry you entered '+guess+".")
    print('The answer was mouse.')
# prompt player to play again

#    - program restarts if player chooses to play again
#    - otherwise program terminates
reply = input("Play again? y/n")
