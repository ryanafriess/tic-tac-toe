import math
import random
global size
size = 3

def possibleMoves(brd):
    return {pos for pos, val in enumerate(brd) if val == "."}

def makeMove(brd, tkn, idx):
    return brd[:idx] + tkn + brd[idx+1:]

def printBoard(board):
    print("\n".join([board[i:i+size] for i in range(0, size*size, size)]))

def ticTacToeCt(brd, tkn):
    count = 0
    TLBR = [brd[pos] for pos in range(0, size*size, size+1)]
    TRBL = [brd[pos] for pos in range(size-1, size*size-(size-1), size-1)]

    if len(set(TLBR)) == 1 and tkn in TLBR:
        count += 1
    if len(set(TRBL)) == 1 and tkn in TRBL:
        count += 1
    
    for row in range(size):
        rowVals = brd[row*size:row*size + size]
        if len(set(rowVals)) == 1 and tkn in rowVals:
            count += 1
    for col in range(size):
        colVals = brd[col:size*size:size]
        if len(set(colVals)) == 1 and tkn in colVals:
            count += 1

    return count

def scoreGame(brd):
    if ticTacToeCt(brd, "x") > 0:
        return 1
    if ticTacToeCt(brd, "o") > 0:
        return -1
    else:
        return 0
    
def isFinished(brd): 
    if scoreGame(brd) != 0:
        return True
    if "." in brd:
        return False
    return True

    
def runGame(brd):
    tokenToPlay = "x"
    while not isFinished(brd):
        possibles = [*possibleMoves(brd)]
        brd = makeMove(brd, tokenToPlay, random.choice(possibles))
        if tokenToPlay == "x":
            tokenToPlay = "o"
        else:
            tokenToPlay = "x"
        #printBoard(brd)
        #print("--------")
    return brd

def runGames():
    cases = set()
    games = 0
    for i in range(10000000000):
    
        brd = runGame("."*size*size)
        games += 1
        if not brd in cases:
            cases.add(brd)
            print(brd, len(cases), games)

def negamax(board, depth, alpha, beta, player):
    if isFinished(board): return player * scoreGame(board)
    bestValue = -math.inf
    for move in possibleMoves(board):
        newBoard = makeMove(board, "x" if player == 1 else "o", move)
        value = -negamax(newBoard, depth-1, -beta, -alpha, 1 if player == -1 else -1)
        bestValue = max(bestValue, value)
        alpha = max(alpha, value)
        if alpha >= beta:
            break
    return bestValue

def getBestMove(board, player):
    bestMove = None
    bestValue = -math.inf
    moves = list(possibleMoves(board))
    random.shuffle(moves) 

    for move in moves:
        newBoard = makeMove(board, player, move)
        value = -negamax(newBoard, 9, -math.inf, math.inf, -1 if player == "x" else 1)
        if value > bestValue:
            bestValue = value
            bestMove = move
    return bestMove

def playGame():
    board = "."*size*size
    print("---")
    printBoard(board)
    player = "x"
    while not isFinished(board):
        if player == "x":
            move = int(input("Enter move (index): "))
            print("---")
        else:
            move = getBestMove(board, player)
        board = makeMove(board, player, move)
        print("---")
        printBoard(board)
        player = "o" if player == "x" else "x"
    print("Game Over")
    
playGame()