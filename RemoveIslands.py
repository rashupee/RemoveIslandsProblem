# Remove Islands

# Implement in python

# Given a 2D Matrix representing a black & white image, remove islands that are l,r and u,d isolated from a black
# pixel at the boundary

# Matrix is called M[i][j]
#	i is row
#	j is column



# Useful function definition
# 	connected(i,j) takes a coordinate and decides whether nearest neighbors offer potential connection to a black
#	boundary pixel

# returns Boolean value

# We will restrict usage to i,j NOT on the boundary
# This will not be good for small matrices len(M[0]) < 3, or len(M) < 3

# M is global


def connected(i,j):
	return M[i-1][j]==1 or M[i][j-1]==1 or M[i+1][j]==1 or M[i][j+1]==1


def boundaryElement(i,j):
	# Returns true if i,j is an index of an edge element
	return i == 0 or i == len(M) - 1 or j == 0 or j == len(M[0]) - 1

def displayArray(M):	
	for row in M:
		print(''.join(str(x) for x in row))


# It's got to be a recursive process. Where do I start the process? At the middle? This might be the symmetric choice.
#	connected is a symmetric function

# If I start at the middle of M:
#	If (i,j) is 1 and is not connected:
#		make it a zero
# 	else:
#		move out to surrounding ring


# Non-recursive process is to check every interior pixel.
# Start process from left side, then from the right, then from the top, then from the bottom?


# Let's just implement the simplest thing and see what happens:

# M = [[0,0,0,0,0],
# 	 [0,0,1,1,0],
# 	 [0,0,0,1,0],
# 	 [0,1,1,1,0],
# 	 [1,1,0,0,0],
# 	 [0,0,0,0,0]]


M = [[0,0,1,0,0],
	 [0,0,1,1,0],
	 [0,0,0,1,0],
	 [0,1,1,0,0],
	 [1,1,0,0,0],
	 [0,0,0,0,0]]


# Get array sizes:
rowCount = len(M)
columnCount = len(M[0])



# Create record where we will record peninsulas of M:
N = [ [0] * columnCount for _ in range(rowCount)]

# print("N before we copy M's boundary:")
# print(N)



# Cause N's edges to be the same as M's:
N[0] = M[0]
N[rowCount - 1] = M[rowCount - 1]
for row in range(rowCount):
    N[row][0] = M[row][0]
    N[row][columnCount-1] = M[row][columnCount-1]

# print("N after we copied over M's boundary:")
# print(N)


def sweepFrom(i,j):
	# Go above
	if not boundaryElement(i-1,j):
		if N[i-1][j] != 1:
			if M[i-1][j] == 1:
				N[i-1][j] = 1
				sweepFrom(i-1,j)
	# Go down
	if not boundaryElement(i+1,j):
		if N[i+1][j] != 1:
			if M[i+1][j] == 1:
				N[i+1][j] = 1
				sweepFrom(i+1,j)
	# Go right
	if not boundaryElement(i,j+1):
		if N[i][j+1] != 1:
			if M[i][j+1] == 1:
				N[i][j+1] = 1
				sweepFrom(i,j+1)
	# Go left
	if not boundaryElement(i,j-1):
		if N[i][j-1] != 1:
			if M[i][j-1] == 1:
				N[i][j-1] = 1
				sweepFrom(i,j-1)


def applySweepFromBoundary():
	# Corners don't matter
	# From upper boundary
	i = 0
	j = 0
	while j < columnCount - 1:
		if N[i][j] == 1:
			sweepFrom(i+1,j)
		j += 1
	# print("Upper boundary must have gone well")
	# From lower boundary
	i = rowCount - 1
	j = 1
	while j < columnCount - 1:
		if N[i][j] == 1:	
			sweepFrom(i-1,j)
		j += 1

	# From left boundary
	i = 1
	j = 0
	while i < rowCount - 1:
		if N[i][j] == 1:
			sweepFrom(i,j+1)
		i += 1

	# From right boundary
	i = 1
	j = columnCount - 1
	while i < rowCount - 1:
		if N[i][j] == 1:
			sweepFrom(i,j-1)
		i += 1


print("M is:")
displayArray(M)

print("N before sweeping is:")
displayArray(N)

applySweepFromBoundary()

print("N after sweeping is:")
displayArray(N)


