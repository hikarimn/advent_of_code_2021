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

def check_for_winners(boards):
    # return a list of indexes of the winning boards
    winners_indexes = set()
    for i, board in enumerate(boards):
        for n in range(5):
            if all(element == 'X' for element in board[n]): winners_indexes.add(i)
        
        for n in range(5):
            vertical_list = []
            for m in range(5): vertical_list.append(board[m][n])
            if all(element == 'X' for element in vertical_list): winners_indexes.add(i)

    return list(winners_indexes) if len(winners_indexes) != 0 else None

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

def delete_boards_with_indexes(boards, indexes):
    for index in sorted(indexes, reverse=True):
        del boards[index]
    return boards

def play_bingo(numbers, boards):
    for num_index, num in enumerate(numbers):
        boards = mark_a_number(boards, num)
        winning_board_indexes = check_for_winners(boards)

        if winning_board_indexes is None: continue
        if len(boards) == 1:
            unmarked_sum = get_sum_of_unmarked_numbers(boards, boards[winning_board_indexes[0]])
            return unmarked_sum * int(num)

        boards = delete_boards_with_indexes(boards, winning_board_indexes)

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