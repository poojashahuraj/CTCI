"""
There is an array with every element repeated twice except one. Find that element?
{1, 1, 2, 2, 3, 3, 4, 4, 5}

questions to ask interviewer:
is given array sorted or un sorted?
does not matter actually, brute force approach can be store each element and its count in hash table,
then iterate through hashtable keys and whos occurence is 1 return that element.
Run time is o(n) for storing each element in an array and then may be o(n/2) to iterate through keys of dictionary,
plus we are using extra space here to store key as element and occurence as value whihc is o(n/2)+1


## so use xor instead, u need to iterate through the list only once means runtime is o(n) and space complexity is only o(1)
e.g. 1^2^3^4^3^2^1 will give you 4, xor operation commutative and associative means seq of operations does not matter.
remember any element XORed with 0 , gives same element, e.g. 0^7=7, 5^5=0
XOR is nothing but all different bits are set to 1.
"""


def find_single_occur_element(ip_arr):
    op = 0
    for i in ip_arr:
        op = op ^ i
    if not op:
        print "All the elements in given input array apprear twice."
    return op
print find_single_occur_element([1, 1, 2, 2, 3, 3, 4, 4, 5])
print find_single_occur_element([7, 5, 3, 1, 3, 7, 5])
print find_single_occur_element([6, 2, 4, 4, 6, 2])

# 1 1 0 0
# 1 0 1 0
# ----------------
# 1 0 0 0      AND
# 1 1 1 0      OR
# 0 1 1 0      XOR

# All elements appear thrice in the given array, return the non repeating element
def single(array):
    ones, twos = 0, 0
    for x in array:
        ones = (ones ^ x) & ~twos
        twos = (ones & x) | (twos & ~x)
        """
        twos |= ones & x
        ones ^= x
        not_threes = ~(ones & twos)
        ones &= not_threes
        twos &= not_threes
        """
    assert twos == 0
    return ones
print single([1,1,1,2])
#single([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5])

# given a list of integers find two non repeating ints
# [2,4,7,9,2,4] ans is 7, 9

def find_nums(ip_arr):
    xor =0
    for i in ip_arr:
        xor = xor ^ i
    # now find the rightmost bit set in xor, that is where is right where first two integers differ
    # e.g. XOR =1110 , then first bit differs at position 1
    bit_set = xor & ~(xor-1)
    first_set =[]
    second_set = []
    for i in ip_arr:
        if i & bit_set == bit_set:
            first_set.append(i)
        else:
            second_set.append(i)
    print first_set, second_set
    # take XOR of each element and then return the value
    f = 0
    for i in first_set:
        f = f^i
    sec = 0
    for i in second_set:
        sec = sec ^ i
    return f,sec

print find_nums([2,4,7,9,2,4])
