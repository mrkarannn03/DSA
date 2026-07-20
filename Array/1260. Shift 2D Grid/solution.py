class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        m = len(grid)
        n = len(grid[0])
        l = [num for row in grid for num in row]
        k = k % (m * n)

        l = l[-k:] + l[:-k]

        return [l[i * n : i * n + n] for i in range(m)]
