# Problem 6
def filter_return_tuple(predicate, seq):
    return tuple(x for x in seq if predicate(x))


# reduce : fn(a,a) -> a, seq, a, r type: a
def my_reduce(fn, seq, initial):
    it = iter(seq)
    if initial is None:
        val = next(it)
    else:
        val = initial
    for x in it:
        val = fn(val, x)
    return val


# Problem 7
def filter_using_reduce(predicate, seq):
    def f(total, current):
        if predicate(current):
            return total + [current]
        return total
    return reduce(f, seq, [])


# Problem 7
def map_using_reduce(fn, seq):
    def f(total, current):
        return total + [fn(current)]
    return reduce(f, seq, [])


if __name__ == '__main__':
    print filter_using_reduce(lambda x: x == 1, range(3))
    print map_using_reduce(lambda x: x+1, range(3))

