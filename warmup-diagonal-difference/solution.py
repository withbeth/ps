#!/bin/python
# refer : https://www.hackerrank.com/challenges/diagonal-difference/problem

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    if len(arr) < 2:
        return 0
    return abs(sum(get_diagonal_left_gen(arr))
               - sum(get_diagonal_right_gen(arr)))


def get_diagonal_left_gen(seq):
    for i in xrange(len(seq)):
        yield seq[i][i]


def get_diagonal_right_gen(seq):
    for i in xrange(len(seq)):
        yield seq[len(seq) - 1 - i][i]


if __name__ == '__main__':

    n = int(raw_input())

    arr = []
    for _ in xrange(n):
        arr.append(map(int, raw_input().rstrip().split()))

    print arr
    print diagonalDifference(arr)







