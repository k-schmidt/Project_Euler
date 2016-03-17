'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get
3, 5, 6, and 9. Ths sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''
from functools import partial


def multiple(denominator, numerator):
    return numerator % denominator == 0

is_multiple3 = partial(multiple, 3)
is_multiple5 = partial(multiple, 5)


def is_multiple_3_or_5(number):
    return is_multiple3(number) or is_multiple5(number)


def sum_of_multiples(ceiling):
    return sum(filter(is_multiple_3_or_5, xrange(ceiling)))

if __name__ == '__main__':
    print sum_of_multiples(1000)
