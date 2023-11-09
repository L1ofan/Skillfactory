board = list(range(1,10))

def vizyal_board(board):
    for i in range(3):
        print('|', board[0+i*3],'|', board[1+i*3],'|', board[2+i*3],'|')

def write_input(player_write):
    valid = False
    while not valid:
        player_other = input('Выбирите клетку' + player_write + '? ')
        try:
            player_other = int(player_other)
        except:
            print("Некоректный ввод. Проверьте и напишите снова")
            continue
        if player_other >= 1 and player_other <= 9:
            if (str(board[player_other -1]) not in "ХО"):
                board[player_other-1] = player_write
                valid = True
            else:
                print("Эта клетка уже занята")
        else:
            print("Некоректный ввод. Введите число от 1 - 9 что бы сделать ход")

def check_win(board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
             return board[each[0]]
    return False

def main(board):
    counter = 0
    win = False
    while not win:
        vizyal_board(board)
        if counter % 2 == 0:
            write_input("X")
        else:
            write_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print(tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
    vizyal_board(board)

main(board)