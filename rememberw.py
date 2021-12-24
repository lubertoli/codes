# Remember The Word Design
# clear screen
# display header
print("-" * 80)
print("Remember The Word")
print("-" * 80)

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
# display four words
#   - display word one at a time
#   - 1 sec pause before the word disappears and the next word appears
#   - words are chosen randomly from a list
#   - words start with different letters
import time
print('orange')
time.sleep(1)
print('chair')
time.sleep(1)
print('sandwich')
time.sleep(1)
print('mouse')
time.sleep(1)
# prompt player to enter a word that starts with a particular letter
guess = input("What word starts with the letter c?")
#   - answer is chosen randomly from the four words that are displayed
#   - use first letter of answer to prompt player
# evaluate answer
# display feedback
#   - congratulations message is displayed if player answers correctly
print('Congratulations,you are correct!')
#   - otherwise condolence message
print('Sorry you entered '+guess+".")
# prompt player to play again

#    - program restarts if player chooses to play again
#    - otherwise program terminates
reply = input("Play again? y/n")
