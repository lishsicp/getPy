# write your code here


win_count = 0
winner = ''
cells = []

current_player = 'O'
cells = '_________'
cells = cells.replace('_', ' ').upper()
cells = list(cells)

def board_display():
    print("---------")
    print("|", cells[0], cells[1], cells[2], "|")
    print("|", cells[3], cells[4], cells[5], "|")
    print("|", cells[6], cells[7], cells[8], "|")
    print("---------")
    return

board_display()

# def no_winner(cells):
    
            
def diagonal_win(cells):
    global win_count
    global winner
    if cells[0] == cells[4] == cells[8] != ' ':
        win_count += 1
        winner = cells[0] + ' wins'
        return True
    elif cells[2] == cells[4] == cells[6] != ' ':
        win_count += 1
        winner = cells[2] + ' wins'
        return True

def horizontal(cells):
    global win_count
    global winner
    for i in range(0, 7, 3):
        if cells[i] == cells[i + 1] == cells[i + 2] != ' ':
            win_count += 1
            winner = cells[i]
            return True

def vertical(cells):
    global win_count
    global winner
    for i in range(0, 3):
        if cells[i] == cells[i + 3] == cells[i + 6] != ' ':
            win_count += 1
            winner = cells[i]
            return True

def check_for_index(a, b):
    i = a - 1
    j = b + 2
    num = (i * 3 + j) - 3
    return num

while True:
    if win_count == 1:
        break
    coordinates = input('Enter the coordinates: ').split()
    index = check_for_index(int(coordinates[0]), int(coordinates[1]))
    if coordinates[0].isalpha() or coordinates[1].isalpha():
        print('You should enter numbers!')
    elif int(coordinates[0]) < 1 or int(coordinates[0]) > 3 or int(coordinates[1]) < 1 or int(coordinates[1]) > 3:
        print("Coordinates should be from 1 to 3!")
    elif cells[index] == 'X' or cells[index] == 'O':
        print("This cell is occupied! Choose another one!")
    else:
        # cells[index] = current_player
        if current_player == 'O':
            current_player = 'X'
            cells[index] = current_player
        elif current_player == 'X':
            current_player = 'O'
            cells[index] = current_player
        board_display()
        horizontal(cells)
        vertical(cells)
        diagonal_win(cells)
        count = 0
        for i in range(len(cells)):
            if cells[i] == ' ':
                count += 1
        if count == 0:
            print('Draw')
            break
# no_winner(cells)

if win_count == 1:
    if horizontal(cells):
        print(winner + ' wins')
    elif vertical(cells):
        print(winner + ' wins')
    elif diagonal_win(cells):
        print(winner)
    

