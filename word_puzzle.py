import random
def instructions():
    #reads and displays instructions for the game
    filename = 'wp_instructions.txt'
    file_mode = 'r'
    infile = open(filename,file_mode)
    content = infile.read()
    infile.close()
    print(content)

def choose_word():
    #chooses a random word for the player to guess from a list of words 
    possible_words = ['apple','banana','watermelon','kiwi','pineapple','mango']
    word = random.choice(possible_words)
    return word

def prompt_for_guess(count):
    #prompts player to guess a letter and and keeps track of how many guesses the player has left
    guess = input('Guess a letter (' +  str(count)  +' guesses remaining): ')
    return guess

def display_result(word,correct_letters):
    #displays the letters the player got right so far
    c=''
    for letter in correct_letters:
        c = c + letter
        
    print('The answer so far is '+' '.join(c))    
        
def evaluate_guess(word,guess,correct_letters,count):
    #checks if guess is a letter in word
    #if not the number of guesses remaining goes down
    letters = list(word)
    if guess in letters:
        if guess in correct_letters:
            count = count - 1
            
        else:
            for i in range(0,len(word)):
                if letters[i] == guess:    
                    correct_letters[i] = guess
                   
    else: 
        count = count - 1 
    return correct_letters, count
        
def end_game(word,correct_letters):
    #terminates the game and prints message of congratulations if word guesses or condolensce if word not guessed
    if list(word) == correct_letters:
        print('Good job! You found the word '+word+'!')
    else:
        print('Not quite, the correct word was '+word+'. Better luck next time')
    input('Press enter to end the game.')          
              
def main():
    instructions()
    word = choose_word()
    count = 4
    correct_letters = ['_']*len(word)
    while count > 0 and '_' in correct_letters:
        display_result(word,correct_letters)
        guess = prompt_for_guess(count)
        answer = evaluate_guess(word,guess,correct_letters,count)//
        count = answer[1]
        correct_letters = answer[0]
    end_game(word,correct_letters)        
main()    