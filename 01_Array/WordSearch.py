"""
Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally
 or vertically neighboring. The same letter cell may not be used more than once.
For example,
Given board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]


word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
"""
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        visited = []
        for i in xrange(len(board)):
            visited.append([False] * len(board[0]))

        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self.existRecur(board, visited, i, j, word, 0):
                    return True
        return False


    def existRecur(self, board, visited, i, j, word, index):
        if index == len(word):
            return True

        if i < 0 or i == len(board) or j < 0 or j == len(board[0]) or visited[i][j] or board[i][j] != word[index]:
            return False

        visited[i][j] = True
        if self.existRecur(board, visited, i-1, j, word, index+1) or \
            self.existRecur(board,visited, i+1, j, word, index+1) or \
            self.existRecur(board,visited, i, j-1, word, index+1) or \
            self.existRecur(board, visited, i, j+1, word, index+1):
            print([i, j])
            return True
        visited[i][j] = False

if __name__ == "__main__":
    solution = Solution()
    print(solution.exist([['A','B','C','E'],  ['S','F','C','S'],  ['A','D','E','E']], "ABCCED"))

