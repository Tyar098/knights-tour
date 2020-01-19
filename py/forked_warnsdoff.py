from heapq import heappush, heappop # for priority queue
import random
import string
cbx = 5; cby = 5 # width and height of the chessboard
cb = [[0 for x in range(cbx)] for y in range(cby)] # chessboard
# directions the Knight can move on the chessboard
dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]
# start the Knight from a random position
kx = 0
ky = 0

def isInBoard(x, y, n, board):
	if (x >= 0 and x < n and y >= 0 and y < n and board[y][x] == 0):
		return True

	return False

for k in range(cbx * cby):
    cb[ky][kx] = k + 1
    pq = [] # priority queue of available neighbors
    for i in range(8):
        nx = kx + dx[i]; ny = ky + dy[i]
        if isInBoard(nx, ny, cbx, cb):
        # if nx >= 0 and nx < cbx and ny >= 0 and ny < cby and cb[ny][nx] == 0:
            # count the available neighbors of the neighbor
            ctr = 0
            for j in range(8):
                ex = nx + dx[j]; ey = ny + dy[j]
                if isInBoard(ex, ey, cbx, cb):
                # if ex >= 0 and ex < cbx and ey >= 0 and ey < cby and cb[ey][ex] == 0: 
                    ctr += 1
            heappush(pq, (ctr, i))
    # move to the neighbor that has min number of available neighbors
    if len(pq) > 0:
        (p, m) = heappop(pq)
        kx += dx[m]; ky += dy[m]
    else: break

# print cb
for cy in range(cby):
    for cx in range(cbx):
        print string.rjust(str(cb[cy][cx]).zfill(2), 2),
    print