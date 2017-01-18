"""
By definition of prime! An integer greater
than one is called a prime number if its only positive divisors (factors) are one and itself.
"""


class PrimeNumber(object):
    def __init__(self):
        pass

    def is_prime(self, num):
        if num == 0 or num == 1:
            print "BY definition prime number should be greater that 1"
            return False
        elif num == 2:
            return True
        else:
            for i in range(2, num):
                if num % i == 0:
                    return False
            return True

    def get_all_primes(self, num):
        ret_list = []
        for i in range(num + 1):
            if self.is_prime(i):
                ret_list.append(i)
        return ret_list


p = PrimeNumber()
print p.is_prime(5)
print p.is_prime(13)
print p.is_prime(3456781)
print p.get_all_primes(13)
print p.get_all_primes(3456781)
