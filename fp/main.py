from solution import *

if __name__ == '__main__':
    def print_fn(x):
        print x

    #my_map(print_fn, range(10))
    #print_fn(my_reduce(lambda x, y: x+y, range(5), 0))
    print_fn(my_reduce_right(lambda x, y: x+y, range(5), 0))
