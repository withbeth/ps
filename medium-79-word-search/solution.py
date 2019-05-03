#! /bin/python
from Queue import Queue


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # visited map - key : (i,j), val: bool
        # letter2coord map key: letter, val : coord(i,j) list
        # q
        if len(word) == 0:
            return False
        visited = self.get_visited_map(board)
        found_result = []
        for current in self.letter2coord(word[0], board):
            if not visited[current]:
                #found_result.append(self.explore(current, word, board, visited))
                found_result.append(self.explore_dfs(current, 0, word, board, visited))
        return len(filter(lambda b: b is True, found_result)) > 0

    def explore(self, start, word, board, visited):
        print "Start explore.."
        found_size = 0
        current_idx = 0
        q = Queue()
        q.put(start)
        while not q.empty():
            current = q.get()
            if not visited[current]:
                print "[Current:", self.coord2letter(current, board), current, "]"
                visited[current] = True
                map(q.put, self.get_unvisited_neighbors(current, current_idx, word, board, visited))
                for nxt in self.get_unvisited_neighbors(current, current_idx, word, board, visited):
                    print "[Neighbor: ", self.coord2letter(nxt, board), nxt, " ]"
                found_size = found_size + 1
                current_idx = current_idx + 1

        return len(word) == found_size

    def explore_dfs(self, current, current_idx, word, board, visited):
        if len(word) - 1 == current_idx:
            print "Founded!"
            return True
        if not visited[current]:
            print "[Current:", self.coord2letter(current, board), current, "]"
            visited[current] = True

            for nxt in self.get_unvisited_neighbors(current, current_idx, word, board, visited):
                print "[Neighbor: ", self.coord2letter(nxt, board), nxt, " ]"
            for nxt in self.get_unvisited_neighbors(current, current_idx, word, board, visited):
                if self.explore_dfs(nxt, current_idx + 1, word, board, visited):
                    return True
                else:
                    print "  Make visit false to..", self.coord2letter(current, board), current
                    print "  Make visit false to..", self.coord2letter(nxt, board), nxt
                    visited[current] = False
                    visited[nxt] = False


        print "Not Founded..."
        return False

    def get_unvisited_neighbors(self, current, current_idx, word, board, visited):
        nxt_idx = current_idx + 1
        if nxt_idx < len(word):
            for nxt in self.get_neighbor_candidates_coords(current):
                if nxt in visited \
                    and not visited[nxt] \
                        and self.coord2letter(nxt, board) == word[nxt_idx]:
                    yield nxt

    def get_neighbor_candidates_coords(self, current):
        i, j = current
        return [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]

    def get_visited_map(self, board):
        return {(i, j): False
                for i, j, _
                in self.get_coord_and_letter(board)}

    def coord2letter(self, coord, board):
        i, j = coord
        return board[i][j]

    def letter2coord(self, letter, board):
        # Or it'd be better to just had a map
        for i, j, other_letter in self.get_coord_and_letter(board):
            if letter == other_letter:
                yield (i, j)

    def get_coord_and_letter(self, board):
        for i, row in zip(xrange(len(board)), board):
            for j, letter in zip(xrange(len(row)), row):
                yield (i, j, letter)

