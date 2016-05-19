"""
Formula for any rectangular grid (nxm)
(n+m)! // (n! x m!)
"""
from functools import reduce


def factorial(number):
    return reduce(lambda x, y: x * y, range(1, number + 1))

def main(x, y):
    return factorial(x + y) // factorial(x) // factorial(y)

if __name__ == '__main__':
    print(main(20,20))
