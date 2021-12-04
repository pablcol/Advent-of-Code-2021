input = open("day04/inputd4.txt", "r")

bingo_numbers = list(map(int, next(input).split(",")))

boards = []
for row in input:
    row = row.strip()
    if row == "":
        board = []
        boards.append(board)
        continue
    board += map(int, row.split())


def wins(board: list):
    for i in range(0, 5):
        if all(n < 0 for n in board[5 * i:5 * i + 5]):
            return True
        if all(n < 0 for n in board[i::5]):
            return True
    return False


def first_winner():
    for number in bingo_numbers:
        for i in range(len(boards)):
            boards[i] = [n if n != number else -1 for n in boards[i]]
            if wins(boards[i]):
                return number * sum(n for n in boards[i] if n >= 0)


def last_winner():
    for number in bingo_numbers:
        winners = []
        for i in range(len(boards)):
            boards[i] = [n if n != number else -1 for n in boards[i]]
            if wins(boards[i]):
                if len(boards) == 1:
                    return number * sum(n for n in boards[i] if n >= 0)
                winners.append(boards[i])
        for board in winners:
            boards.remove(board)


print(first_winner())
print(last_winner())
