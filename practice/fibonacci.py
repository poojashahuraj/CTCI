"""
There are n stairs, a person standing at the bottom wants to reach the top.
The person can climb either 1 stair or 2 stairs at a time.
Count the number of ways, the person can reach the top.
"""


class Fibonacci(object):
    def __init__(self):
        pass

    # Program to display the Fibonacci sequence up to n-th term where n is provided by the user
    def print_fibbo(self, length):
        n1 = 0
        n2 = 1
        count = 2
        result = []
        result.extend([n1, n2])
        if length <= 0:
            print("Please enter a positive integer")
            return -1
        elif length == 1:
            print("Fibonacci sequence upto", length, ":")
        else:
            print("Fibonacci sequence upto", length, ":")
            while count < length:
                nth = n1 + n2
                n1 = n2
                n2 = nth
                count += 1
                result.append(nth)
        return result

    def get_nth_element_fibbo(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.get_nth_element_fibbo(n - 1) + self.get_nth_element_fibbo(n - 2)

a = Fibonacci()
print a.print_fibbo(6)
print a.get_nth_element_fibbo(10)


# stair case problem