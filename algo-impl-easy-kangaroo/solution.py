#! /bin/python

# Constraints
# 0 <= x1 <= x2 <= 10^4
# 1 <= v1 <= 10^4
# 1 <= v2 <= 10^4
def kangaroo(x1, v1, x2, v2):
    if not verify_pre_conditions(x1, v1, x2, v2):
        return yes_or_no(False)
    return yes_or_no(can_reach_same_position(x1, v1, x2, v2))


def yes_or_no(boolean):
    if boolean:
        return "YES"
    return "NO"


def can_reach_same_position(x1, v1, x2, v2):
    if x1 == x2:
        return v1 == v2
    return (x2 - x1) % (v1 - v2) == 0


def verify_pre_conditions(x1, v1, x2, v2):
    if x1 == x2:
        return v1 == v2
    elif x1 < x2:
        return v1 > v2
    return v1 < v2
