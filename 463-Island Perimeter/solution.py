class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def get_score(grid, i, j):
            score = 0
            #check up
            if i == 0:
                score += 1
            elif i != 0 and grid[i-1][j] == 0:
                score += 1

            #check down
            if i == len(grid) - 1:
                score += 1
            elif i != len(grid) - 1 and grid[i+1][j] == 0:
                score += 1

            #check left
            if j == 0:
                score += 1
            elif j != 0 and grid[i][j-1] == 0:
                score += 1

            #check right
            if j == len(grid[i]) - 1:
                score += 1
            elif j != len(grid[i]) - 1 and grid[i][j+1] == 0:
                score += 1

            return score
        
        perimeter = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    perimeter += get_score(grid,i,j)
        
        return perimeter
