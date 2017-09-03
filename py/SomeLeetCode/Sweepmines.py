def updateBoard(board, click):
    x = click[0]
    y = click[1]
    if board[x][y] == 'M':
        board[x][y] = 'X'
        return board
    else:
        board = DFS(board,click)
    return board

def DFS(board,click):
    x = click[0]
    y = click[1]
    mines = 0
    neighbour = []
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if x+i>=0 and x+i<len(board) and y+j >=0 and y+j<len(board[0]):
                if board[x+i][y+j] == 'M':
                    mines += 1
                elif mines == 0 and board[x+i][y+j] == 'E' :
                    neighbour.append([x+i, y+j])
    if mines > 0:
        board[x][y] = str(mines)
    else:
        for c in neighbour:
            if c == click:
                board[x][y] = 'B'
            else:
                board = DFS(board, c)
    return board




a = ["B1E1B","B1X1B","B111B","BBBBB"]
a = list(map(lambda x: list(x), a))
b = [1,2 ]
print(updateBoard(a,b))