def set_boards(lines):
    boards = []

    for index, line in enumerate(lines):
        if len(line) <= 1:
            if index != 0: boards.append(board)
            board = []
        else: 
            board.append(line.split())
    boards.append(board)
    return boards

def check_for_a_winner(boards):
    # return the index of the board (ith board of boards) if it has at least one complete row or column of marked numbers else return null
    for i, board in enumerate(boards):
        for n in range(5):
            if all(element == 'X' for element in board[n]): return i
        
        for n in range(5):
            vertical_list = []
            for m in range(5): vertical_list.append(board[m][n])
            if all(element == 'X' for element in vertical_list): return i

def get_sum_of_unmarked_numbers(boards, board):
    sum = 0
    for row in range(5):
        for col in range(5):
            if board[row][col] == 'X': continue
            sum += int(board[row][col])
    return sum

def mark_a_number(boards, number):
    for board in boards:
        for row in range(5):
            for col in range(5):
                if not board[row][col] == number: continue
                board[row][col] = 'X'
    return boards

def play_bingo(numbers, boards):
    for num in numbers:
        boards = mark_a_number(boards, num)
        winning_board_index = check_for_a_winner(boards)
        if winning_board_index is not None:
            unmarked_sum = get_sum_of_unmarked_numbers(boards, boards[winning_board_index])
            return unmarked_sum * int(num)

f = open("input.txt", "r")
lines = f.readlines()
f.close()

numbers = lines[0].split(',')
boards = set_boards(lines[1:])
print(play_bingo(numbers, boards))


# def pretty_print_board(board):
#     print('\n'.join('{}' for _ in range(len(board))).format(*board))
#     print()

# def pretty_print(boards):
#     for board in boards:
#         pretty_print_board(board)
#         print()

        # # check diagonally
        # diagnoal_list_1 = []
        # diagnoal_list_2 = []
        # for n in range(5): 
        #     diagnoal_list_1.append(board[n][n])
        #     diagnoal_list_2.append(board[n][4-n])
        # if all(element == 'X' for element in diagnoal_list_1): return i
        # if all(element == 'X' for element in diagnoal_list_2): return i