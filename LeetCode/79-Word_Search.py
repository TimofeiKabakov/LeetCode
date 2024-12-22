class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        movement = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()

        def dfs(i, j, ind):
            if i < 0 or i == ROWS or j < 0 or j == COLS or (i, j) in visited:
                return False

            if board[i][j] != word[ind]:
                return False
            
            if ind == len(word) - 1:
                return True

            visited.add((i, j))

            for move in movement:
                new_i = i + move[0]
                new_j = j + move[1]
                if dfs(new_i, new_j, ind + 1):
                    return True
            
            visited.remove((i, j))

            return False

        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0):
                    return True

        return False
