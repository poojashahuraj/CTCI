"""
You have a list of integers, and for each index you want to find the product of every integer except the integer
at that index.
input:  [1, 7, 3, 4]
output: [84, 12, 28, 21]
"""


class Multiplication(object):
    def __init__(self):
        pass

    def multiplication(self, ip_lst):
        """
        run time complexity is o(n^2) as we have two cascade for loops.
        """
        result_arr = [0] * len(ip_lst)
        for index, value in enumerate(ip_lst):
            val = 1
            p = ip_lst[:index] + ip_lst[index + 1:]
            for j in p:
                val = val * j
            result_arr[index] = val
        return result_arr

    def get_multiplication(self, ip_lst):
        """
        This method gives better time complexity as we run throguh full list only twice.
        :param ip_lst:
        :return:
        """
        before = self.products_of_all_ints_before_index(ip_lst)
        after = self.products_of_all_ints_after_index(ip_lst)
        op_lst = [None] * len(after)
        for i in range(len(before)):
            op_lst[i] = before[i] * after[i]
        return op_lst

    def products_of_all_ints_before_index(self, ip_lst):
        result_arr = [None] * len(ip_lst)
        val = 1
        for index, value in enumerate(ip_lst):
            result_arr[index] = val
            val = val * value
        return result_arr

    def products_of_all_ints_after_index(self, ip_lst):
        result_arr = [None] * len(ip_lst)
        product_so_far = 1
        for index, value in enumerate(reversed(ip_lst)):
            result_arr[index] = product_so_far
            product_so_far = product_so_far * value
        return result_arr


m = Multiplication()
print m.get_multiplication([1, 7, 3, 4])

class ConvertToBinary(object):
    def __init__(self):
        pass

    def convert_int_to_binary(self, num):
        if num == 0:
            return 0
        if num == 1:
            return 1
        current = num
        result_str = ""
        while current != 0:
            remainder = current % 2
            current = current / 2
            result_str += str(remainder)
            self.convert_int_to_binary(current)
        return result_str[::-1]

    def convert_fraction_to_binary(self, num):
        result = []
        for i in range(len(num)):
            num = list(num)[i::]
            float_num = self.get_num_from_list(num)
            if float_num *2 > 1:
                result.append(1)
            else:
                result.append(0)
        op = ""
        for j in result:
            op = op + str(j)
        return op

    def convert_decimal_to_binary(self, num):
        num_lst = str(num).split(".")
        a = self.convert_int_to_binary(int(num_lst[0]))
        b = self.convert_fraction_to_binary(num_lst[1])
        return str(a)+"."+str(b)

    def get_num_from_list(self, lst):
        result_str = "0."
        for i in lst:
            result_str +=str(i)
        return float(result_str)

    # Write a function to determine the number of bits required to convert integer A to integer B
    # e.g A 32: 11111 ,
    #     B 14: 01110
    # Now the answer is 2 because only 2 bits are different.
    def xor_two_nums(self, a, b):
        op = bin(a ^ b)
        diff_bit = op.count("1")
        print "Number {}:{} and {}:{} differs in {} bits".format(a, b, bin(a), bin(b), diff_bit)
        return op.count("1")

if __name__ == '__main__':
    c2b = ConvertToBinary()
    for i in range(8):
        print c2b.convert_int_to_binary(i)
    print c2b.convert_decimal_to_binary(7.235)
    c2b.xor_two_nums(32,14)
