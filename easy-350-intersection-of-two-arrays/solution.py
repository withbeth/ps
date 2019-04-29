#! /bin/python


# Constraint
# list1, list2 can have duplicated elements
def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    xs = sorted(nums1)
    ys = sorted(nums2)
    if xs == ys:
        return xs
    if len(xs) == 0 or len(ys) == 0:
        return []
    if len(xs) > len(ys):
        return get_intersection(ys, xs)
    return get_intersection(xs, ys)


def get_intersection(ss, ls):
    """
    :param ss: short seq
    :param ls: long seq
    :return: intersected elements list
    """
    def remove_and_return_elem_if_exists(s):
        if s in ls:
            ls.pop(ls.index(s))
            return s
        return None
    return filter(lambda x: x is not None, map(remove_and_return_elem_if_exists, ss))





