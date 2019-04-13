from solution import *

if __name__ == '__main__':

    # FP style list
    xs = pair(3)(pair(2)(pair(1)(None)))
    head = fst
    tail = snd
    array = list2array(xs)
    print array
    print array2list(array)
    print array2list(str2array("Hello"))
    print fp_range(1)(10)
    print list2array(fp_map(fizzbuzz)(fp_range(1)(50)))




