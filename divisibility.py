"""
Answer the question does m divide n in linear time with respect to
the numerator.

Comments should give enough clarity that the proof can be easily
completed from reading.

For numerator of length n and denominator of length m, this first
iteration requires N * D runtime. Where N is the length of the numerator
and D is the length of the denominator.

"""


def last_digit_in_base(n, m):
    '''Return the last digit of n in base m.'''
    # linear time preprocessing to get n to look like an array.
    if m > n:
        return n
    n = reversed(bin(n)[2:])

    increment = 1
    total = 0
    for i in n:  # n times
        # Without the optimizations below, this would convert n to base m.
        # Comparisons and addition take linear time.  These operations,
        # therfore, each take len(total), len(m), or len(increment) time.
        if i == '1':
            total += increment
        increment += increment

        # Calculate increment modulo m.
        # increment never exceeds 2*m.
        # len(increment) never exceeds len(m) + 1
        if increment > m:
            increment -= m

        # Dido for total
        if total > m:
            total -= m
    return total


def divides(m, n):
    '''Return whether m divides n.'''
    return last_digit_in_base(m, n) == 0


'''
The code above is a fairly straightforward algorithm.

The comparisons and the additions above can be easily optimized away.
The main question is whether or not the subtractions can be given
that one term remains constant in all of them.
'''


class CircularBitArray(list):
    def __init__(self, len):
        i = 0
        while i < len:
            i += 1
            list.append(self, 0)
