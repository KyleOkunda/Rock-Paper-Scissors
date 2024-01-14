import random
options = {
    '1': 'rock',
    '2': 'paper',
    '3': 'scissors',
    '4': 'quit'
}
player_points = 0
pc_points = 0
tries = 0
while tries < 3:
    tries += 1
    move = input('Go: ')
    comp = str(random.choice(range(1, 4)))
    players_move = options.get(move)
    pc_move = options.get(comp)


    if players_move == 'quit':
        break
   
    def moves_made ():
        print(f'Your move: {options.get(move)}')
        print( f'Computer: {options.get(comp)}')


    if (move in options) == False:
        print('Invalid choice')
    elif players_move == pc_move:
        moves_made()
        print('Draw')
    elif (players_move == 'rock'and pc_move == 'scissors') or (players_move == 'paper' and pc_move == 'rock') or (players_move == 'scissors' and pc_move == 'paper'):
        player_points += 1
        moves_made()
        print('You win')
    elif (players_move == 'rock'and pc_move != 'scissors') or (players_move == 'paper' and pc_move != 'rock') or (players_move == 'scissors' and pc_move != 'paper'):
        pc_points += 1
        moves_made()
        print('You lose')
    
if player_points == pc_points:
    print(f'You have {player_points}')
    print("It's a draw.")
elif player_points > pc_points:
    print(f'You have {player_points} points') 
    print('Congrats, You Win!')
elif pc_points > player_points:
    print(f'Computer has {pc_points} points')
    print('Better luck next time')