class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS  = len(heights), len(heights[0])
        movements = [[0, 1], [0, -1], [1, 0] , [-1, 0]]
        atlantic, pacific = set(), set()
        result = []

        def dfs(i, j, curSet, prevHeight):
            if (i < 0 or i >= ROWS or 
                j < 0 or j >= COLS or 
                (i, j) in curSet or 
                heights[i][j] < prevHeight
            ):
                return
            
            curSet.add((i, j))

            for mov in movements:
                new_i = i + mov[0]
                new_j = j + mov[1]
                dfs(new_i, new_j, curSet, heights[i][j])

        for i in range(ROWS):
            dfs(i, 0, pacific, 0)
            dfs(i, COLS - 1, atlantic, 0)

        for j in range(COLS):
            dfs(0, j, pacific, 0)
            dfs(ROWS - 1, j, atlantic, 0)

        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) in atlantic and (i, j) in pacific:
                    result.append([i, j])

        return result
    
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)