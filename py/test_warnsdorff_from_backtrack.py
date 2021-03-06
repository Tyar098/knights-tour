from heapq import heappush, heappop

# STUB for dev
n = 5
start_x = 0
start_y = 0

print("n, x, y: ", n, start_x, start_y)
print("\n")

# n = input("board size: ")

# start_x = int(input("x: "))
# while start_x < 0 or start_x > n:
#     print ("x diluar matriks papan! x harus diantara 0 {0}".format(n))
#     start_x = int(input("x : "))

# start_y = int(input("y: "))
# while start_y < 0 or start_y > n:
#     print ("y diluar matriks papan! y harus diantara 0 {0}".format(n))
#     start_y = int(input("y : "))


board = [[-1 for x in range(n)] for y in range(n)]

move_x = [2, 1, -1, -2, -2, -1, 1, 2]
move_y = [1, 2, 2, 1, -1, -2, -2, -1]

def isInBoard(x, y, board, n):
	if (x >= 0 and x < n and y >= 0 and y < n and board[y][x] == -1):
		return True

	return False

def resolveKTWD(start_x, start_y, board, n):
	
	for k in range(n**2):
		# print (k)
		board[start_y][start_x] = k
		pq = []  # priority queue of available neighbors

		for i in range(8): # mencari jalur
			new_x = start_x + move_x[i]
			new_y = start_y + move_y[i]

			if isInBoard(new_x, new_y, board, n):
				ctr = 0
				for j in range(8): # -- mencari derajat dari setiap jalur
					ex = new_x + move_x[j]
					ey = new_y + move_y[j]

					if isInBoard(ex, ey, board, n):
						ctr += 1
				print(ctr) ;heappush(pq, (ctr, i))

		# memindahkan jalur yang mempunyai derajat terkecil		
		if len(pq) > 0:
			(p, m) = heappop(pq)
            # print (p, m)

			start_x += move_x[m]
			start_y += move_y[m]
			
		else:
			break


if (not resolveKTWD(start_x, start_y, board, n)):	
	for cy in range(n):
		for cx in range(n):
			print(str(board[cy][cx]).zfill(2), end=' ')
		print()
else:
	print("Solution does not exist")
	