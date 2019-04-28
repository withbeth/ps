def simple_sum(ar=[]):
    return reduce(lambda x, y: x + y, ar, 0)


def prefix_sum(ar=[]):
    prefix=[]
    for a in ar:
        if len(prefix) == 0:
            prefix.append(a)
        else:
            prefix.append(prefix[-1] * a)
    return prefix


def suffix_sum(ar=[]):
    suffix=[]
    ar.reverse()
    for a in ar:
        if len(suffix) == 0:
            suffix.append(a)
        else:
            suffix.append(suffix[-1] * a)
    return suffix.reverse()


if __name__ == '__main__':

    print prefix_sum([1,2,3,4])
    print suffix_sum([1,2,3,4])
    print simple_sum(range(1,4))

