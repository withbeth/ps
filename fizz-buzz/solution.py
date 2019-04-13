# FP Style restrictions
# 1. Function with only 0 or 1 arguments
# 2. Function is a single(One line) return
# 3. No loop
# 4. No Ifs
# 5. No Assignments in function
# 6. No side-effects
# 7. No Arrays
def add(a):
    return lambda b: a + b


def sum(i):
    return 0 if (i == 0) else i + sum(i-1)


def pair(first):
    return lambda second: (first, second)


def fst(pair):
    return pair[0]


def snd(pair):
    return pair[1]


# This is a convenient method for converting FP list to imperative programming list
def list2array(xs):
    array = []
    while xs is not None:
        array.append(fst(xs))
        xs = snd(xs)
    return array


# This is a convenient method for converting imperative programming array to FP list
def array2list(array=[]):
    result = None
    array.reverse()
    for e in array:
        result = pair(e)(result)
    return result


def str2array(str=""):
    return [c for c in str]


def fp_range(low):
    def f(high):
        return None if low > high else pair(low)(fp_range(low + 1)(high))
    return f


def fp_map(f):
    def g(xs):
        return None if xs is None else pair(f(fst(xs)))(fp_map(f)(snd(xs)))
    return g


# I guess this is all I can do by using python to comply with fp style restrictions...
def fizzbuzz(n=0):
    def f():
        return "Fizz" if (n % 3 == 0) else ''
    def g():
        return "Buzz" if (n % 5 == 0) else ''
    return f() + g()
