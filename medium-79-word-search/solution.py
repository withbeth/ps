#! /bin/python
from Queue import Queue


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(word) == 0:
            return False
        if not board or len(board[0]) == 0:
            return False

        for start in self.letter2rc(word[0], board):
            if self.dfs(start, word, board):
                return True
        return False

    def dfs(self, current_rc, remaining_letters, board):
        if len(remaining_letters) == 0:
            return True
        if not self.is_in_board(current_rc, board) \
                or not self.rc2letter(current_rc, board) == remaining_letters[0]:
            return False

        # Avoid visiting again
        board[current_rc[0]][current_rc[1]] = '*'

        # Sum result(True, False) of traversing sub-tree candidates
        subtree_res = reduce(lambda t, c: t + c,
                             map(lambda nxt: self.dfs(nxt, remaining_letters[1:], board),
                                 self.get_subtree_candidates(current_rc)))
        # Re-set
        board[current_rc[0]][current_rc[1]] = remaining_letters[0]

        return subtree_res

    def is_in_board(self, current, board):
        i, j = current
        r = len(board[0])
        c = len(board)
        return 0 <= i < c and 0 <= j < r

    def get_subtree_candidates(self, current):
        i, j = current
        return [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]

    def rc2letter(self, coord, board):
        i, j = coord
        return board[i][j]

    def letter2rc(self, letter, board):
        for i, j, other in self.iter_board(board):
            if letter == other:
                yield (i, j)

    def iter_board(self, board):
        for i in xrange(len(board)):
            for j, letter in zip(xrange(len(board[0])), board[i]):
                yield (i, j, letter)

