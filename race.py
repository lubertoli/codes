import random
def roll_die(player):
    # rolls die
    input('Player '+ player + ' press enter to roll!')
    number_rolled = random.randint(1,6)
    print('Player '+ player + ' rolled a ' +str(number_rolled))
    return number_rolled

def update_position(lane, number_rolled,player):
    # updates the position of both players in lane
    if player == 'x':
        #start, when none of the players have played yet
        if 'x' and 'o' not in lane:
            lane[number_rolled] = 'x'
            position_x = lane.index('x')
            lane[0] = 'o'
    
        elif number_rolled + lane.index('x') < len(lane):
            position_x = lane.index('x')
            position_o = lane.index('o')
            # x kicks o to the start position
            if position_x + number_rolled == position_o:
                lane[0]= 'o'            
                lane[position_x + number_rolled] = 'x'
                lane[position_x] = '-'
                print('x kicked the rival!')
            # x moves to new position
            else:
                lane[position_x + number_rolled] = 'x'
                lane[position_x] = '-'
    
        else:
            print('The roll was too high, player x stays in this position') 
    if player == 'o':
        # first time o plays
        if lane[0] == 'o':
            position_x = lane.index('x')
            # o kicks x to the start position
            if number_rolled == position_x:
                lane[number_rolled] = 'o'
                position_o = lane.index('o')            
                lane[0] = 'x'
                print('o kicked the rival!')
            else:
                # o moves to new position
                lane[number_rolled] = 'o'
                position_o = lane.index('o') 
                lane[0] = '-'
        elif number_rolled + lane.index('o') < len(lane):
            position_x = lane.index('x')
            position_o = lane.index('o')
            # o kicks x to the start position
            if position_o + number_rolled == position_x:
                lane[0]= 'x'            
                lane[position_o + number_rolled] = 'o'
                lane[position_o] = '-'
                print('o kicked the rival!')
            else:
                # o moves to new position
                lane[position_o + number_rolled] = 'o'
                lane[position_o] = '-'           
        
        else:
            print('The roll was too high, player o stays in this position')         
        
         
            
        return lane                     
    
def display_state(lane):
    # prints lane with current state of the game
    header = ('*')*36
    print(header)
    c=''
    for i in lane:
        c = c + i
    print('update: '+' '.join(c)) 
    print(header)
 
def opponent(player):
    # changes the turn after each move
    if player == 'x':
        player = 'o'
    else:
        player = 'x'
    return player    

def check_game_over(lane,continue_game):
    # ends the game and prints the winner
    if lane[-1] == 'x':
        print('Player x has won!')
        continue_game = False
    elif lane[-1] == 'o':
        continue_game = False
        print('Player o has won!')
    return continue_game    
        

def main():
    player = 'o'
    print('Players begin in the starting postion')
    print('*','-','-','-','-','-','-','-')
    lane = ['-']*8
    continue_game = True
    while continue_game:
        player = opponent(player)
        number_rolled = roll_die(player)
        results = update_position(lane,number_rolled,player)
        display_state(lane)
        continue_game = check_game_over(lane,continue_game)
main()        
        

    
    

    
    
    
    


    

    
          




