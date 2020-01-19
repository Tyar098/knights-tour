import sys
import time
import itertools
import threading
import upsidedown

# -- cek apakah x dan y masih didalam matriks
def isInBoard(x, y, board, n):

    if(x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1):
        return True

    return False


# -- fungsi untuk print matriks jika terdapat solusi
def printSolution(board, n):
    for i in range(n):
        for j in range(n):
            print(str(board[i][j]).zfill(2), end=' ')
        print()
    # time.sleep(5)


# return false jika tidak ada solusi,
# return true dan exit jika di temukan solusi pertama
def solveKT():
    count = 0
    steps = []

    # input board size
    n = int(input("board size: "))

    # input x
    start_x = int(input("x : "))
    while start_x < 0 or start_x > n:
        print ("x diluar matriks papan! x harus diantara 0 {0}".format(n))
        start_x = int(input("x : "))

    # input y
    start_y = int(input("y : "))
    while start_y < 0 or start_y > n:
        print ("y diluar matriks papan! y harus diantara 0 {0}".format(n))
        start_y = int(input("y : "))

    t = threading.Thread(target=animate)
    t.start()
    # n = 6
    # start_x = 0
    # start_y = 0

    # Init Board matrix (list)
    board = [[-1 for i in range(n)]for i in range(n)]
    # print (board)

    # pergerakan kuda
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    # posisi pertama kuda
    board[start_x][start_y] = 0

    # Counter posisi kuda
    pos = 1

    # Cek solusi
    global done

    if(not recurseKT(board, start_x, start_y, move_x, move_y, pos, n)):
        done = True
        flushLoading()
        print("Solution does not exist")
    else:
        done = True
        flushLoading()
        printSolution(board, n)


# -- fungsi rekursif
def recurseKT(board, curr_x, curr_y, move_x, move_y, pos, n):

    if(pos == n**2):
        return True

    # coba ke-8 possibility
    for i in range(8):

        global count
        count = count + 1

        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        # print ("moving to {0} {1}..".format(new_x, new_y))
        
        if(isInBoard(new_x, new_y, board, n)):
            # print ("movement to {0} {1} is Safe".format(new_x, new_y))
            board[new_x][new_y] = pos
            
            # Backtracking
            if(recurseKT(board, new_x, new_y, move_x, move_y, pos+1, n)):
                return True

            board[new_x][new_y] = -1

    return False


# -- animasi loading
def animate():
    asa = upsidedown.transform('  ..')
    for c in itertools.cycle(['..  ', ' : ', asa, ':  ']):
        if done:
            break
        sys.stdout.write('\rLoading ' + c)
        sys.stdout.flush()
        time.sleep(0.05)
    sys.stdout.write('\rDone!     \r')

# -- flush animasi loading
def flushLoading():
  return time.sleep(1), sys.stdout.flush()

# main function
if __name__ == "__main__":
    done = False
    count = 0
    start = time.process_time()
    
    solveKT()
    end = time.process_time()
    timeExec = end - start

    print ("1. Backtracking")
    print ("{0} attempts ends in {1} seconds".format(count, timeExec))
