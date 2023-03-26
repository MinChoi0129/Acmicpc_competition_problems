number_of_coin = 0

a, b = map(int, input().split())
before = []
for _ in range(a):
    line = list(input())
    number_of_coin += line.count('O')
    before.append(line)

c, d = map(int, input().split())
after = []
for _ in range(c):
    after.append(list(input()))

def generateCombinedBoard(before, after, dx, dy):
    board = [[0] * (2*b-2+d) for _ in range(2*a-2+c)]
    for mx in range(c):
        for my in range(d):
            if after[mx][my] == 'O':
                board[(a-1) + mx][(b-1) + my] += 1
    
    for mx in range(a):
        for my in range(b):
            if before[mx][my] == 'O':
                board[mx + dx][my + dy] += 1

    return board

def countIntersection(board):
    result = 0
    for line in board:
        result += line.count(2)
    return result


answer = int(1e9)
for dx in range(a+c-1):
    for dy in range(b+d-1):
        new_board = generateCombinedBoard(before, after, dx, dy)
        intersection = countIntersection(new_board)
        answer = min(answer, number_of_coin - intersection)

print(answer)