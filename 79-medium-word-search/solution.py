#! /bin/python


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

        def is_in_board(current):
            i, j = current
            r = len(board[0])
            c = len(board)
            return 0 <= i < c and 0 <= j < r

        def get_possible_subtrees(current, next_letters):
            if len(next_letters) == 0:
                return []
            i, j = current
            return [(x, y)
                    for x, y
                    in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
                    if is_in_board((x, y)) and board[x][y] == next_letters[0]]

        def dfs(current, next_letters):
            i, j = current
            if not next_letters:
                return True

            # Avoid visiting again
            origin, board[i][j] = board[i][j], '*'

            found = False
            for nxt in get_possible_subtrees(current, next_letters):
                if dfs(nxt, next_letters[1:]):
                    found = True
                    break

            # Re-set
            board[i][j] = origin
            return found


        for start in self.letter2rc(word[0], board):
            if dfs(start, word[1:]):
                return True
        return False

    def letter2rc(self, letter, board):
        for i, j, other in self.iter_board(board):
            if letter == other:
                yield (i, j)

    def iter_board(self, board):
        for i in xrange(len(board)):
            for j, letter in zip(xrange(len(board[0])), board[i]):
                yield (i, j, letter)

