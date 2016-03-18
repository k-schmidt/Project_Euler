import itertools


def get_smaller_list(x):
    return [i for i in xrange(2, x)
            if x % i != 0]


def small_multi(x):
    l = get_smaller_list(x)
    for i in itertools.count():
        if i == 0:
            continue
        large_number = x * i
        if all(large_number % j == 0 for j in l):
            yield large_number


if __name__ == "__main__":
    print get_smaller_list(20)
    g = small_multi(20)
    print g.next()
