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
#                    - player can play the game multiple times
#Remember Version 4  - identify non-adjacent duplicate line groups
#                    - define a function
#                    - place the line group in the body of the function
#                    - replace all occurences of the line group with a call to the user defined function
# Key Points about User defined functions - Section 1.6
import time, os, random

def display_header():
    # clears the screen and displays the header
    #return a None object
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
    
def sample_words():
    # returns a list of 4 words that are randomly chosen from a file
    filename = 'words.txt'
    file_mode = 'r'
    infile = open(filename, file_mode)
    all_words = infile.read()
    all_words_list = all_words.splitlines()
    words = random.sample(all_words_list,4)
    return words #throw

def display_instructions(filename):
    #displays instructions
    #returns None
    #filename = "intructions.txt"
    file_mode = 'r'
    infile = open(filename,file_mode)
    content = infile.read() # read is a method call
    infile.close()
    print(content)    

def display_words(words):
    #display words
    # - words is a parameter of type list - holds the list of words that are to be displayed
    pause_time = 1
    for word in words:
        print(word)
        time.sleep(pause_time)
        display_header()

def prompt_for_guess(start_letter):
    # prompts the player to enter a word that starts with a particular letter
    guess = input('What word starts with the letter '+start_letter+'?') #start_letter is the parameter
    return guess

def display_result(guess,answer):
    #evaluates and displays the result
    if guess.lower() == answer.lower():
        #   - congratulations message is displayed if player answers correctl
        print('Congratulations,you are correct!')
        print('The answer was '+answer+'.')
    else:
        #   - otherwise condolence message
        print('Sorry you entered '+guess+".")
        print('The answer was '+answer+'.')  
        
def prompt_to_continue():
    #prompts the player to restart game
    filename = input('Enter filename ')
    reply = input('Play again?y/N').lower
    continue_game = reply == 'y'
    return continue_game
    
def main():
    #main program starts here
    continue_game = True
    filename = 'instructions.txt'
    while continue_game:
        display_header()
        
        # display instructions
        display_instructions(filename)
        
        # prompt player to press enter
        input("Press enter key to display the words.") # Ignore the return object from the input function
        
        display_header() 
        
        # sample words
        words = sample_words() #catch
        
        answer = random.choice(words)
        start_letter = answer[0]
        display_words(words)  #function call    
           
        # prompt player to enter a word that starts with a particular letter
        guess = prompt_for_guess(start_letter) #start_letter is the argument
        
        #   - answer is chosen randomly from the four words that are displayed
        #   - use first letter of answer to prompt player
        # evaluate answer and display feedback
        display_result(guess,answer)
        
       
        # prompt player to play again
        #    - program restarts if player chooses to play again
        continue_game = prompt_to_continue()
        
main()