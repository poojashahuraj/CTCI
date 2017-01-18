# How can you quickly compute 2^x?
class FastestTwoPower(object):
    def __init__(self):
        pass

    @staticmethod
    def calculate(power):
        return 1 << power

    @staticmethod
    def is_power_of_2(num):
        """
        Fastest way to check is given number is power of two.
        """
        return num != 0 and ((num & (num - 1)) == 0)


f = FastestTwoPower()
print f.calculate(3)
print f.is_power_of_2(4)
