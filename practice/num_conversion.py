import string


class NumberConversion(object):
    def __init__(self, num, base):
        self._num = num
        self._base = base
        self._dict_a = {}
        alphabets = list(string.ascii_lowercase)
        numbers = [i for i in range(10, 10 + len(alphabets))]
        for i in range(len(alphabets)):
            self._dict_a[numbers[i]] = alphabets[i]

    def convert_to_given_base(self):
        current_num = self._num
        new_num = ''
        while current_num != 0:
            remainder = current_num % self._base
            current_num = current_num / self._base
            if 37 > remainder > 9:
                remainder_str = self._dict_a[remainder]
            elif remainder >= 36:
                remainder_str = "(" + str(remainder) + ")"
            else:
                remainder_str = str(remainder)
            new_num = remainder_str + new_num
        return new_num


print NumberConversion(8, 2).convert_to_given_base()
print NumberConversion(155, 16).convert_to_given_base()
print NumberConversion(15, 132).convert_to_given_base()
print NumberConversion(40, 132).convert_to_given_base()


def convert_num_to_binary(num):
    op = ""
    while num != 0:
        remainder = num % 2
        num /= 2
        op = str(remainder)+op
    return op
print "Convert a num to binary"
for i in range(20):
    print "Decimal:{} binary:{}".format(i, convert_num_to_binary(i))
#=======================================================================


dict_b = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "a":10,
          "b":11, "c":12, "d":13, "e":14, "f":15}


def convert_hex_to_decimal(num_str):
    l = len(num_str)
    num = 0
    power = 0
    for i in range(l-1, -1, -1):
        num += dict_b[num_str[i]] * pow(16, power)
        power += 1
    return num
print "***************************"
print "converting hex to decimal"
print "Hex:{}, Decimal:{}".format("90",convert_hex_to_decimal("90"))
print "Hex:{}, Decimal:{}".format("ab1",convert_hex_to_decimal("ab1"))

#=======================================================================
# ip:1234 op:4321
def reverse_num(num):
    stack = []
    for i in num:
        stack.append(i)
    op = ""
    while stack:
        op +=stack.pop()
    return op
print reverse_num("1234")