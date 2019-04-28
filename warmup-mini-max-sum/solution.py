#!/bin/python
# refer : https://www.hackerrank.com/challenges/mini-max-sum/problem
# Note : given num of integers is fixed to 5

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    min_sum = pow(10, 9) * 5
    max_sum = 1
    total = sum(arr)
    for i in arr:
        current_sum = total - i
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < min_sum:
            min_sum = current_sum
    return min_sum, max_sum


if __name__ == '__main__':
    arr = map(int, raw_input().rstrip().split())

    print arr
    print miniMaxSum(arr)
