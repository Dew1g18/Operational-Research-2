import numpy as np

A1 = [
    [-1,4,-1,-1],
    [-1,-1,7,10],
    [-1,-1,-1,1],
    [-1,-1,-1,-1]]

A2 = [
    [-1,2,10,-1,-1,-1],
    [-1,-1,0,-1,12,-1],
    [-1,-1,-1,1,-1,-1],
    [-1,-1,-1,-1,0,3],
    [-1,-1,-1,-1,-1,5],
    [-1,-1,-1,-1,-1,-1]]

A3 = [
    [-1, 2, 10, -1, -1, -1],
    [-1, -1, 0, -1, 12, -1],
    [-1, -1, -1, 1, -1, -1],
    [-1, -1, -1, -1, 0, 3],
    [-1, -1, -1, -1, -1, 5],
    [-1, -1, -1, -1, -1, -1]]

def EET(A, i):
    # i-=1  #Modified i as index starts at 0 and nodes start at 1  (now modified inline to save lines lmao)
    smallX = -1,0 ## distance, node
    for x in range (0, len(A[i-1])-1):
        if A[x][i-1]>=smallX[0] and A[x][i-1]!=-1: smallX=A[x][i-1],x+1
    if smallX[1] == 0: return 0 # This is for the first ordinate as the method will run through
    else: return EET(A, smallX[1]) + smallX[0] # recursively finds the next in the list to cumulatively build EET


    ##returns the Earliest expected arrival of the node i, from the matrix A

def LET(A,i):
    # i-=1 #Modified i as index starts at 0 and nodes start at 1  (now modified inline to save lines lmao)
    smallLET = np.Infinity, 0 #Distance , node
    outNodes = []
    for x in range (0, len(A[i-1])):
        if A[i-1][x]!=-1:
            outNodes.append(x) # This finds all of the arcs exiting the current node
    for x in outNodes: # Now only looking through the arcs exiting the given node
        dist = LET(A, x+1)-A[i-1][x]
        if (dist)<smallLET[0]:
            smallLET = (dist), x+1 # Reassigning the LET value when conditions are met.
    if smallLET[1]==0: return EET(A,i)
    else: return smallLET[0]

    ##returns the Latest expected arrival of i from A


## As we have been instructed to use as few lines as possible, this has meant that I have not included any
## error handling and assumed perfect input for each of the given methods.
def TF(A, i, j):
    return LET(A,j) - EET(A, i) - A[i-1][j-1] #Directly from the formula in the notes



# print(LET(matrix,2))

# Finds all arcs in a given graph and runs them, for testing
def TFtester(mat):
    for i in range(0, len(mat)):
        for j in range(0, len(mat)):
            if (mat[i][j]!=(-1) and mat[i][j]!=0):
                print(f"The TF of {i+1} to {j+1} if {TF(mat, i+1, j+1)}")

# tests LET EET and TF
def TestAll(mat):
    for i in range (1, len(mat)+1):
        print (f"EET of {i}= {EET(mat, i)}")
    print("\n")
    for i in range(1, len(mat) + 1):
        print (f"LET of {i}= {LET(mat, i)}")
    print("\n")
    TFtester(mat)
        # print (f"TF of {i} and {i+1} = {TF(A2, i, i+1)}")

# TestAll(A3)


