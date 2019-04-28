#!/bin/python

from itertools import permutations

ALL_MAGIC_SQUARE = []

# Complete the formingMagicSquare function below.
def formingMagicSquare(square):
    def get_cost(magic_square):
        return sum([abs(src_cell - target_cell)
                    for src_cell, target_cell
                    in zip(square2list(magic_square), square2list(square))])

    return min(map(get_cost, ALL_MAGIC_SQUARE))


def pretty_print(square):
    def print_row(xs):
        print xs[0], xs[1], xs[2]
    map(print_row, square)


def square2list(square):
    return [x for row in square for x in row]


def list2square(xs):
    return [xs[0:3],
            xs[3:6],
            xs[6:9]]


def get_rows(square):
    for row in square:
        yield row


def get_cols(square):
    yield square[0][0], square[1][0], square[2][0]
    yield square[0][1], square[1][1], square[2][1]
    yield square[0][2], square[1][2], square[2][2]


def get_digs(square):
    yield [row[idx] for idx, row in zip(range(0, 3), square)]
    yield [row[idx] for idx, row in zip(range(0, 3), reversed(square))]


def is_magic_square(square):
    # 1. Each cell contains a diff int
    # 2. Sum of the ints in each row, col and diagonal is equal
    sum_set = (set(map(sum, get_rows(square)))
               | set(map(sum, get_cols(square)))
               | set(map(sum, get_digs(square))))
    return len(sum_set) == 1


if __name__ == '__main__':

    ALL_MAGIC_SQUARE = filter(is_magic_square,
                              map(list2square,
                                  permutations(range(1, 10))))
    s = []
    for _ in xrange(3):
        s.append(map(int, raw_input().rstrip().split()))
    print(formingMagicSquare(s))


