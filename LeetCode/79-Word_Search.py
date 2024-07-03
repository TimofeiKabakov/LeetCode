class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        i_add_ind = [1, -1, 0, 0]
        j_add_ind = i_add_ind[::-1]

        def wordSearch(i: int, j: int, index: int, visited):
            # Check for an already visited cell
            if (i, j) in visited:
                return False

            # Check for indices out of boundaries
            if index >= len(word) or i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False

            # Check if the next cell letter matches the one in the word
            if word[index] != board[i][j]:
                return False

            # Check if we reached the end of the word
            if index + 1 == len(word):
                return True

            visited.add((i, j))

            for iterator in range(4):
                if wordSearch(i + i_add_ind[iterator], j + j_add_ind[iterator], index + 1, visited.copy()):
                    return True
            
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if wordSearch(i, j, 0, set()):
                    return True