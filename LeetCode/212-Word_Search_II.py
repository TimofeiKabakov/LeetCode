class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
    def addWord(self, word: str):
        trieNode = self
        for c in word:
            if c not in trieNode.children:
                trieNode.children[c] = TrieNode()
            trieNode = trieNode.children[c]
        trieNode.endOfWord = True

def print_trie(node, level):
    print(node.children_chars, level)
    for child in node.children_nodes.values():
        print_trie(child, level + 1)

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:        
        def wordSearch(i: int, j: int, current: str, visited, trieNode):
            if (i < 0 or i >= len(board) or j < 0 or j >= len(board[0])
                or (i, j) in visited
                or board[i][j] not in trieNode.children):
                return

            trieNode = trieNode.children[board[i][j]]
            current = current + board[i][j]

            visited.add((i, j))

            if trieNode.endOfWord:
                res.add(current)

            for ind in range(4):
                wordSearch(i + i_add[ind], j + j_add[ind], current, visited, trieNode)

            visited.remove((i, j))

        res = set()
        i_add = [1, -1, 0, 0]
        j_add = i_add[::-1]

        # Construct a Trie
        trieNode = TrieNode() 
        for word in words:
            trieNode.addWord(word)

        for i in range(len(board)):
            for j in range(len(board[0])):
                wordSearch(i, j, "", set(), trieNode)

        return list(res)