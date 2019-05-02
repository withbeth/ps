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
        board_info_gen = self.get_board_info_gen(board)
        board_map = self.get_board_map(board_info_gen)
        checked_map = self.get_checked_map(board_info_gen)

        word_idx = 0
        while word_idx < len(word):
            return False

        return True

    def recur(self, board_map={}, checked_map={}, word="", word_idx=0):
        if len(word) == word_idx:
            return False
        letter = word[word_idx]
        if letter not in board_map:
            return False
        for i, j in board_map[letter]:
            if checked_map[(i, j)] is not True:
                checked_map[(i, j)] = True
                return self.recur(board_map, checked_map, word, word_idx+1)

        pass

    def f(self, x, y, letter, board_map, checked_map):
        if not self.has_neighbors():
            return False
        for neighbor in self.get_neighbors():
            pass
        pass

    def get_letter_gen(self, word=""):
        for letter in word:
            yield letter

    def get_checked_map(self, board_info_gen):
        # key: Coordinate tuple(X,Y) value : Bool
        return {(i, j): False for i, j, _ in board_info_gen}

    def get_board_map(self, board_info_gen):
        # key: letter('A'...'Z'), value : coord tuple list (row, col)
        m = {}
        for i, j, letter in board_info_gen:
            if letter in m:
                m[letter].append((i, j))
            else:
                m[letter] = [(i, j)]
        return m

    def get_board_info_gen(self, board):
        for i, row in zip(range(len(board)), board):
            for j, letter in zip(range(len(row)), row):
                yield (i, j, letter)

    def has_neighbors(self, word, word_idx, board_map, checked_map):
        if len(word) == word_idx or len(word) == word_idx + 1:
            return False
        current_letter = word[word_idx]
        next_letter = word[word_idx + 1]

        currnet_coords = self.get_unchecked_coords(board_map[current_letter], checked_map)
        next_coords = self.get_unchecked_coords(board_map[next_letter], checked_map)



        pass

    def get_neighbors(self):
        pass

    def get_unchecked_coords(self, coords=[], checked_map={}):
        return [(x, y) for x, y in coords if checked_map[(x, y)] is False]
