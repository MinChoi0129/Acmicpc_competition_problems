n = int(input())

score_board = {'D': 0, 'P': 0}

def is_gameover():
    d, p = score_board['D'], score_board['P']
    return abs(d - p) >= 2

def main():
    for _ in range(n):
        score_board[input()] += 1
        if is_gameover():
            print("%d:%d" % (score_board['D'], score_board['P']))
            return
    print("%d:%d" % (score_board['D'], score_board['P']))

main()
