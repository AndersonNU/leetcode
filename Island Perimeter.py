<<<<<<< HEAD
# You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid
# cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is
# exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't
# connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and
# height don't exceed 100. Determine the perimeter of the island.
=======
# You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.
# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water,
# and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water'\
#    ' inside that isn't connected to the water around the island). One cell is a square with side length 1.
# The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        islands = 0
        neighbours = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    islands += 1
                    if i < len(grid) - 1 and grid[i+1][j] == 1:
                        neighbours += 1
                    if j < len(grid[i]) - 1 and grid[i][j + 1] == 1:
                        neighbours += 1
        return islands * 4 - neighbours * 2



        # return sum(sum(map(operator.ne, [0] + row, row + [0]))
        #         for row in grid + map(list, zip(*grid)))

grid = [[0,1,0,0],\
 [1,1,1,0],\
 [0,1,0,0],\
 [1,1,0,0]]
object = Solution()
print(object.islandPerimeter(grid))
>>>>>>> b97b2dce9e8eb18a59ad6f1b18e08e996e7bd071
