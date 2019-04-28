def my_map(fn, seq):
    return [fn(xs) for xs in seq]


def my_reduce(fn, seq, initial=0):
    if len(seq) == 0:
        return initial
    else:
        res = initial
        for x in seq:
            print "Seq : " + str(x)
            res = fn(x, res)
            print "Result Fn applied: " + str(res)
        return res


def my_reduce_right(fn, seq, initial=0):
    if len(seq) == 0:
        return initial
    else:
        return fn(seq[0], my_reduce_right(fn, seq[1:], initial))


