#! /bin/python
# refer - https://www.algoexpert.io/questions/River%20Sizes
from Queue import Queue


def riverSizes(matrix):
    """
    :param matrix: two-dimensional array containing only 0s and 1s(1 represents part of a river)
    :return: an array of the sizes of all rivers represented in the input matrix
    """
    # visited map - k: (i,j) of all 1s v: bool
    # queue - (i,j) of all 1s
    # return 0-size filtered one
    res = []
    visited = get_visited_map(matrix)
    q = get_queue(matrix)
    while q.empty() is False:
        current = q.get()
        if not visited[current]:
            res.append(explore(current, visited))
    return filter(lambda x: x > 0, res)


def explore(start, visited):
    found = 0
    q = Queue()
    q.put(start)
    while q.empty() is False:
        current = q.get()
        if not visited[current]:
            visited[current] = True
            found = found + 1
        map(q.put, get_unvisited_neighbors(current, visited))

    return found


def get_unvisited_neighbors(current, visited):
    for nxt in get_neighbor_candidates(current):
        if nxt in visited and not visited[nxt]:
            yield nxt


def get_neighbor_candidates(current):
    i, j = current
    return [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]


def get_queue(matrix):
    q = Queue()
    for i, j, cell in get_coord_and_cell(matrix):
        if cell == 1:
            q.put((i, j))
    return q


def get_visited_map(matrix):
    return {(i, j): False
            for i, j, cell
            in get_coord_and_cell(matrix)
            if cell == 1}


def get_coord_and_cell(matrix):
    for i, row in zip(xrange(len(matrix)), matrix):
        for j, cell in zip(xrange(len(row)), row):
            yield (i, j, cell)
