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

# -- fungsi rekursif
# fungsi backtracking dengan rekursif akan me-return false jika tidak ada solusi,
# dan me-return true dan exit jika di temukan solusi pertama


def solveKT():

    # done = False

    # def animate():
    #     asa = upsidedown.transform('  ..')
    #     for c in itertools.cycle(['..  ', ' : ', asa, ':  ']):
    #         if done:
    #             break
    #         sys.stdout.write('\r' + c)
    #         sys.stdout.flush()
    #         time.sleep(0.1)
    #     sys.stdout.write('\rDone!     \r')

    # t = threading.Thread(target=animate)
    # t.start()

    # input board size
    # n = int(input("board size: "))

    # # input x
    # start_x = int(input("x : "))
    # while start_x < 0 or start_x > n:
    #     print ("x diluar matriks papan! x harus diantara 0 {0}".format(n))
    #     start_x = int(input("x : "))

    # # input y
    # start_y = int(input("y : "))
    # while start_y < 0 or start_y > n:
    #     print ("y diluar matriks papan! y harus diantara 0 {0}".format(n))
    #     start_y = int(input("y : "))

    n = 3
    start_x = 0
    start_y = 0

    # Init Board matrix (list)
    board = [[-1 for i in range(n)]for i in range(n)]
    print (board)

    # knights possible movement
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    # block pertama
    board[start_x][start_y] = 0

    # Step counter for knight's position
    pos = 1

    # Cek solusi
    if(not recurseKT(board, start_x, start_y, move_x, move_y, pos, n)):
        print("Solution does not exist")
    else:
        printSolution(board, n)
        # print (str(tries)+" movement")

    time.sleep(1)
    done = True

# -- fungsi rekursif

lt = 0
def recurseKT(board, curr_x, curr_y, move_x, move_y, pos, n):
    # print ("pos is {0}".format(pos))

    if(pos == n**2):
        return True

    # coba ke-8 possibility
    for i in range(8):
        lt+=1

        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        print ("moving to {0} {1}..".format(new_x, new_y))
        if(isInBoard(new_x, new_y, board, n)):
            print ("movement to {0} {1} is Safe".format(new_x, new_y))
            board[new_x][new_y] = pos
            print("now pos is {0}".format(pos))
            # Backtracking
            if(recurseKT(board, new_x, new_y, move_x, move_y, pos+1, n)):
                # print ("recurseKT")
                return True

            board[new_x][new_y] = -1
            # else:
            #     print ("Not Safe")
    print (lt)
    return False


# Driver program to test above function
if __name__ == "__main__":
    solveKT()

# This code is contributed by AAKASH PAL
