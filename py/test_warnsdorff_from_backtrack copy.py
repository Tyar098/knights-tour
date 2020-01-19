import sys
import time
import itertools
import threading
import upsidedown
from heapq import heappush, heappop

# STUB for dev
# n = input("board size: ")

# start_x = int(input("x: "))
# while start_x < 0 or start_x > n:
#     print ("x diluar matriks papan! x harus diantara 0 {0}".format(n))
#     start_x = int(input("x : "))

# start_y = int(input("y: "))
# while start_y < 0 or start_y > n:
#     print ("y diluar matriks papan! y harus diantara 0 {0}".format(n))
#     start_y = int(input("y : "))

move_x = [-2, -1, 1, 2, -2, -1, 1, 2]
move_y = [1, 2, 2, 1, -1, -2, -2, -1]

move_x = [2, 1, -1, -2, -2, -1, 1, 2]
move_y = [1, 2, 2, 1, -1, -2, -2, -1]


# -- cek apakah x dan y masih didalam matriks
def isInBoard(x, y, n, board):
    if (x >= 0 and x < n and y >= 0 and y < n and board[y][x] == -1):
        return True

    return False


def resolveKTWD(start_x, start_y, n, board):

    # board = [[-1 for x in range(n)] for y in range(n)]

    for k in range(n**2):
            # print (k)
            board[start_y][start_x] = k
            pq = []  # priority queue of available neighbors

            for i in range(8):  # mencari jalur
                new_x = start_x + move_x[i]
                new_y = start_y + move_y[i]

                if isInBoard(new_x, new_y, n, board):
                    ctr = 0
                    for j in range(8):  # -- mencari derajat dari setiap jalur
                        ex = new_x + move_x[j]
                        ey = new_y + move_y[j]

                        if isInBoard(ex, ey, n, board):
                            ctr += 1

                    heappush(pq, (ctr, i))

            # memindahkan jalur yang mempunyai derajat terkecil
            if len(pq) > 0:
                (p, m) = heappop(pq)

                start_x += move_x[m]
                start_y += move_y[m]

            else:
                break


def solveKTWD(start_x, start_y, n):
    board = [[-1 for i in range(n)]for i in range(n)]

    if (not resolveKTWD(start_x, start_y, n, board)):
        printSolution(board, n)
    else:
        print("Solution does not exist")

# -- fungsi untuk print matriks jika terdapat solusi
def printSolution(board, n):
    for i in range(n):
        for j in range(n):
            print(str(board[i][j]).zfill(2), end=' ')
        print()
    # time.sleep(5)


# return false jika tidak ada solusi,
# return true dan exit jika di temukan solusi pertama
def solveKT(start_x, start_y, n):
    count = 0
    steps = []

    # Init Board matrix (list)
    board = [[-1 for i in range(n)]for i in range(n)]

    # posisi pertama kuda
    board[start_x][start_y] = 0

    # Counter posisi kuda
    pos = 1

    # Cek solusi
    global done

    if(recurseKT(board, start_x, start_y, move_x, move_y, pos, n)):
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
        print ("moving to {0} {1}..".format(new_x, new_y))

        if(isInBoard(new_x, new_y, n, board)):
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

    
    start_x = 0
    start_y = 0

    print("n, x, y: ", n, start_x, start_y)
    print("------------------\n")

    done = False
    count = 0
    start = time.process_time()

    solveKT(start_x, start_y, n)

    end = time.process_time()
    timeExec = end - start

    print ("1. Backtracking")
    print ("{0} attempts ends in {1} seconds".format(count, timeExec))

    print("------------------\n")
    # solveKTWD(start_x, start_y, n)
    # t = threading.Thread(target=solveKTWD, kwargs={'start_x': start_x,'start_y': start_y, 'n':n})
    # t.start()

    print("------------------\n")

    
