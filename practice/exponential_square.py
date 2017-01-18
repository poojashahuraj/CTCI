# coding=utf-8
"""
In general, the number of multiplication operations required to compute bⁿ can be reduced
to Θ(log n) by using exponentiation by squaring
"""
class ExponentialSquare(object):
    def __init__(self):
        pass

    def calculate_power(self, base, power):
        if power == 0:
            return 1
        elif power == 1:
            return base
        elif power == 2:
            return base*base
        else:
            if power % 2 == 0:  # meaning power is even.
                return self.calculate_power(self.calculate_power(base, 2), power / 2)
            else:  # meaning power is odd.
                return base * self.calculate_power(self.calculate_power(base, 2), (power - 1) / 2)


e = ExponentialSquare()

print e.calculate_power(35, 35)
