#read instructions
filename = 'instructions.txt'
file_mode = 'r'
infile = open(filename, file_mode)
instructions = infile.read()
infile.close()
print(instructions)
#repeat rounds
rounds_won_p1 = 0
rounds_won_p2 = 0
ties = 0
continue_game = True
while continue_game:
    #repeat 4 times a round
    results_p1 = []
    results_p2 = []
    points_p1 = 0
    points_p2 = 0
    tosses_per_round = 4
    while tosses_per_round > 0:
        #get user input
        guess = (input('Heads or Tails ? Type H or T >')).upper()
        #toss the coin
        import random
        options = ['H','T']
        toss_p1 = random.choice(options)
        toss_p2 = random.choice(options)
        results_p1.append(toss_p1)
        results_p2.append(toss_p2)
        print('Player 1 has tossed '+toss_p1)
        print('Player 2 has tossed '+toss_p2)
        #print results for toss
        if toss_p1 == guess and toss_p2 == guess:
            points_p1 += 1
            points_p2 += 1
            print('Player 1 wins')
            print('Player 2 wins')
        elif toss_p1 == guess:
            points_p1 +=1
            print('Player 1 wins')
        elif toss_p2 == guess:
            points_p2 += 1
            print('Player 2 wins')
        tosses_per_round = tosses_per_round - 1   
    #print round results
    print('ROUND STATS')
    if points_p1 > points_p2:
        rounds_won_p1 += 1
        print('Player 1 wins this round')
    elif points_p2 > points_p1:
        rounds_won_p2 += 1
        print('Player 2 wins this round')
    else:
        ties += 1
        print("It's a tie")
    print('Player 1 points '+ str(points_p1))
    print('Player 2 points '+ str(points_p2))
    print('Player 1 tossed '+ str(results_p1))
    print('Player 2 tossed '+ str(results_p2))
    #identify pair of 'H'
    pair_of_h_p1 = 0
    pair_of_h_p2 = 0
    index = 0
    for index in range(len(results_p1)-1):
        if results_p1[index] == 'H':
            if results_p1[index+1] == 'H':
                pair_of_h_p1 += 1
    for index in range(len(results_p2)-1):
        if results_p2[index] == 'H':
            if results_p2[index+1] == 'H':
                pair_of_h_p2 += 1
    print('H H found in the player 1 sequence '+ str(pair_of_h_p1)+ ' times')
    print('H H found in the player 2 sequence '+ str(pair_of_h_p2)+ ' times')  
    #ask if player wants to play another round
    reply = input('Do you want to play another round? y/n >').lower()
    continue_game = reply == 'y'
#print game results
print('SUMMARY STATS') 
print('number of ties '+ str(ties))
print('number of player 1 wins '+ str(rounds_won_p1))
print('number of player 2 wins '+ str(rounds_won_p2))

          
          
                
        