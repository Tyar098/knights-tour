import sys
import time
import itertools
import threading
import upsidedown
from heapq import heappush, heappop

# created, reformatted and merged by Tyar from various resources
# NOTE below is for dev
# n = 5
# start_x = 0
# start_y = 0

# pergerakan kuda
move_x = [2, 1, -1, -2, -2, -1, 1, 2]
move_y = [1, 2, 2, 1, -1, -2, -2, -1]

# masukkan board size
n = int(input("board size: "))

# masukkan x
try:
    start_x = int(input("start x : "))
except ValueError:
    print(" input only number")
    start_x = int(input("start x : "))

while start_x < 0 or start_x >= n:
    print ("x diluar matriks papan! x harus diantara 0 {0}".format(n))
    start_x = int(input("start x : "))

# masukkan y
try:
    start_y = int(input("start y : "))
except ValueError:
    print(" input only number")
    start_y = int(input("start y : "))

while start_y < 0 or start_y >= n:
    print ("y diluar matriks papan! y harus diantara 0 {0}".format(n))
    start_y = int(input("start y : "))


# return false jika tidak ada solusi,
# return true dan exit jika di temukan solusi pertama
def resolveKTWD(start_x, start_y, n, board, move_x, move_y):

    for k in range(n**2):
        board[start_y][start_x] = k
        pq = []  # priority queue holder

        for i in range(8):  # mencari jalur
            new_x = start_x + move_x[i]
            new_y = start_y + move_y[i]

            if isInBoard(new_y, new_x, board, n):
                ctr = 0
                for j in range(8):  # -- mencari derajat dari setiap jalur
                    ex = new_x + move_x[j]
                    ey = new_y + move_y[j]

                    if isInBoard(ey, ex, board, n):
                        ctr += 1

                global countWD
                countWD += 1

                heappush(pq, (ctr, i)) # push min heap priority queue

        # memindahkan jalur yang mempunyai derajat terkecil
        if len(pq) > 0:
            (p, m) = heappop(pq)

            start_x += move_x[m]
            start_y += move_y[m]

        else:
            break

    for a in board:
        if (-1 in a):
            return False

    return True

# -- fungsi utama
def solveKTWD():
    board = [[-1 for i in range(n)]for i in range(n)]

    if (resolveKTWD(start_x, start_y, n, board, move_x, move_y)):
        for cy in range(n):
            for cx in range(n):
                print(str(board[cy][cx]).zfill(2), end=' ')
            print()
    else:
        print("Solution does not exist")


# return false jika tidak ada solusi,
# return true dan exit jika di temukan solusi pertama
def solveKT():
    count = 0
    steps = []

    t = threading.Thread(target=animate)
    t.start()
    
    # Init Board matrix (list)
    board = [[-1 for i in range(n)]for i in range(n)]

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


# -- fungsi helper cek apakah x dan y masih didalam matriks
def isInBoard(x, y, board, n):

    if(x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1):
        return True

    return False

# -- fungsi helper untuk print matriks jika terdapat solusi
def printSolution(board, n):
    for i in range(n):
        for j in range(n):
            print(str(board[i][j]).zfill(2), end=' ')
        print()
    # time.sleep(5)

# -- fungsi helper animasi loading
def animate():
    asa = upsidedown.transform('  ..')
    for c in itertools.cycle(['..  ', ' : ', asa, ':  ']):
        if done:
            break
        
        sys.stdout.write('\rLoading ' + c)
        sys.stdout.flush()
        time.sleep(0.05)
    sys.stdout.write('\rDone!     \r')

# -- fungsi helper flush animasi loading
def flushLoading():
  return time.sleep(1), sys.stdout.flush()


# main entry function
if __name__ == "__main__":
    done = False
    count = 0
    countWD = 0
    
    print("\n")
    startWD = time.perf_counter()
    print ("1. Warnsdorff'rule ")
    solveKTWD()
    timeExecWD = time.perf_counter() - startWD
    print ("---------------------")
    print ("{0} attempts in {1} seconds".format(countWD, timeExecWD))

    print ("---------------------\n")

    start = time.perf_counter()
    print ("2. Backtracking")
    solveKT()
    print ("---------------------")
    timeExec = time.perf_counter() - start
    print ("{0} attempts in {1} seconds".format(count, timeExec))
    print ("---------------------\n")

    k=input("press enter to exit") 
