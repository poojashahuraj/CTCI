ones = ["", "one", "two", "three", "four", "nine"]
tens = ["ten"]
twenties = []
hundreds = []

def int_2_word(num):
    numeric_str = str(num)
    group_of_numers = []
    for i in range(3,33,3):
        last_bit = numeric_str[-i:]
        q = len(numeric_str)-i
        # 123456
        # for i=3 , last_bit = [4,5,6]
        # for i=6, last_bit = [1, 2, 3, 4, 5, 6]
        if q < -2:
            break
        else:
            if q >= 0:
                group_of_numers.append(int(last_bit[:3]))
            elif q >= -1:
                group_of_numers.append(int(last_bit[:2]))
            elif q >= -2:
                group_of_numers.append(int(last_bit[:1]))
    return group_of_numers

print int_2_word(12345)