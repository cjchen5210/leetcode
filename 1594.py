grid = [[-1,-2,-3],
        [-2,-3,-3],
        [-3,-3,-2]]
def maxProductPath(grid):
	d = dict()
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if j < len(grid[i])-1 and i < len(grid)-1:
				temp = []
				temp.append(grid[i][j+1])
				temp.append(grid[i+1][j])
				d[grid[i][j]] = temp
	print(d)

maxProductPath(grid)