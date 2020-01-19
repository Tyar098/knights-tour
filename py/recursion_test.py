
def solveKTUtil(board, curr_x, curr_y, move_x, move_y, pos, n):
    # print ("pos is {0}".format(pos))
    ''' 
            A recursive utility function to solve Knight Tour 
            problem 
    '''

    if(pos == n**2):
        return True

    # Try all next moves from the current coordinate x, y
    for i in range(8):

        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        if(solveKTUtil(board, new_x, new_y, move_x, move_y, pos+1, n)):
                # print ("solveKTUtil")
                return True

            # Backtracking
    return False


if __name__ == "__main__":
    solveKT()
