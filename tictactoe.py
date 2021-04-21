# write your code here

win_count = 0
winner = ''
def impossible(cells):
    player_x = [i for i in cells if i == 'X']
    player_o = [i for i in cells if i == 'O']
    if abs(len(player_x) - len(player_o)) > 1:
        return True
    
def diagonal_win(cells):
    global win_count
    if cells[0] == cells[4] == cells[8]:
        win_count += 1
        return cells[0] + ' wins'
    if cells[2] == cells[4] == cells[6]:
        win_count += 1
        return cells[2] + ' wins'
            
def horizontal(cells):
    global win_count
    global winner
    for i in range(0, 7, 3):
        if cells[i] == cells[i + 1] == cells[i + 2]:
            win_count += 1
            winner = cells[i]
            return True
                
def vertical(cells):
    global win_count
    global winner
    for i in range(0, 3):
        if cells[i] == cells[i + 3] == cells[i + 6]:
            win_count += 1
            winner = cells[i]
            return True
                
def win_impossible(cells):
    if cells[0] == cells[3] == cells[6] and cells[1] == cells[4] == cells[7]:
        return 1
    elif cells[1] == cells[4] == cells[7] and cells[2] == cells[5] == cells[8]:
        return 1
    elif cells[0] == cells[3] == cells[6] and cells[2] == cells[5] == cells[8]:
        return 1
    elif cells[0] == cells[1] == cells[2] and cells[3] == cells[4] == cells[5]:
        return 1
    elif cells[0] == cells[1] == cells[2] and cells[6] == cells[7] == cells[8]:
        return 1
    elif cells[3] == cells[4] == cells[5] and cells[6] == cells[7] == cells[8]:
        return 1

        
def game_not_finished(cells):
    for i in range(len(cells)):
        if cells[i] == "_":
            return 'Game not finished'
            
cells = input('Enter cells: ')

print('---------')
print('| ' + cells[0] + ' ' + cells[1] + ' ' + cells[2] + ' |')
print('| ' + cells[3] + ' ' + cells[4] + ' ' + cells[5] + ' |')
print('| ' + cells[6] + ' ' + cells[7] + ' ' + cells[8] + ' |')
print('---------')

cells = cells.replace('_', ' ')
current_player = 'X'
coordinates = input('Enter the coordinates: ').split
coo
def insert_in_board(x):
    



horizontal(cells)
vertical(cells)

if impossible(cells) or win_impossible(cells) == 1:
    print("Impossible")
elif horizontal(cells):
    print(winner + ' wins')
elif vertical(cells):
    print(winner + ' wins')
elif diagonal_win(cells):
    print(diagonal_win(cells))
elif game_not_finished(cells):
    print(game_not_finished(cells))
else:
    print("Draw")        
