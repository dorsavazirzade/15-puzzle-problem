
N=4
def getInvCount(arr):
	arr1=[]
	for y in arr:
		for x in y:
			arr1.append(x)
	arr=arr1
	inv_count = 0
	for i in range(N * N - 1):
		for j in range(i + 1,N * N):
			if (arr[j] and arr[i] and arr[i] > arr[j]):
				inv_count+=1
		
	
	return inv_count


def findXPosition(puzzle):
	for i in range(N - 1,-1,-1):
		for j in range(N - 1,-1,-1):
			if (puzzle[i][j] == 0):
				return N - i

def isSolvable(puzzle):
	invCount = getInvCount(puzzle)

	if (N & 1):
		return ~(invCount & 1)

	else:
		pos = findXPosition(puzzle)
		if (pos & 1):
			return ~(invCount & 1)
		else:
			return invCount & 1
	
def solvable_check(puzzle):


         print("The puzzle is Solvable press enter to solve") if  isSolvable(puzzle) else print("Not Solvable")
        
