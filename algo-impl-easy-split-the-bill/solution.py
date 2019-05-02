#! /bin/python
# refer : https://www.hackerrank.com/challenges/bon-appetit/problem

# TODO : Need Monad MayBe or Either

def bonAppetit(bill, k, b):
    """
    bill: an array of integers representing the cost of each item ordered
    - 0 <= bill[i] <= 10^4
    k: an integer representing the zero-based index of the item Anna doesn't eat
    - 0 <= k < n(length of bill array; n should be in arrange of 2<= n <=10^5)
    b: the amount of money that Brian charged Anna for her share of the bill.
    - 0 <= b <= sum(bill)
    """
    actual = sum(exclude(list2map(bill), k).values()) / 2
    if b == actual:
        print "Bon Appetit"
    else:
        print abs(b - actual)


def exclude(m={}, k=0):
    if m[k]:
        del m[k]
    return m


def list2map(l=[]):
    return {i: elem for i, elem in zip(range(len(l)), l)}

