# integer number to english word conversion
# can be used for numbers as large as 999 vigintillion
# (vigintillion --> 10 to the power 60)
# tested with Python24      vegaseat      07dec2006

def int2word(n):
    """
    convert an integer number n into a string of english words
    """
    # break the number into groups of 3 digits using slicing
    # each group representing hundred, thousand, million, billion, ...
    group_of_three = []
    r1 = ""
    # create numeric string
    numeric_string = str(n)
    for k in range(3, 33, 3):
        r = numeric_string[-k:]
        q = len(numeric_string) - k
        # break if end of numeric_string has been reached
        if q < -2:
            break
        else:
            if q >= 0:
                group_of_three.append(int(r[:3]))
            elif q >= -1:
                group_of_three.append(int(r[:2]))
            elif q >= -2:
                group_of_three.append(int(r[:1]))

    number_to_word = ""
    for i, x in enumerate(group_of_three):
        b1 = x % 10
        b2 = (x % 100) // 10
        b3 = (x % 1000) // 100
        # print b1, b2, b3  # test
        if x == 0:
            continue  # skip
        else:
            t = thousands[i]
        if b2 == 0:
            number_to_word = ones[b1] + t + number_to_word
        elif b2 == 1:
            number_to_word = tens[b1] + t + number_to_word
        elif b2 > 1:
            number_to_word = twenties[b2] + ones[b1] + t + number_to_word
        if b3 > 0:
            number_to_word = ones[b3] + "hundred " + number_to_word
    return number_to_word


############# globals ################

ones = ["", "one ", "two ", "three ", "four ", "five ",
        "six ", "seven ", "eight ", "nine "]

tens = ["ten ", "eleven ", "twelve ", "thirteen ", "fourteen ",
        "fifteen ", "sixteen ", "seventeen ", "eighteen ", "nineteen "]

twenties = ["", "", "twenty ", "thirty ", "forty ",
            "fifty ", "sixty ", "seventy ", "eighty ", "ninety "]

thousands = ["", "thousand ", "million "]

if __name__ == '__main__':
    # select an integer number n for testing or get it from user input
    # n = 4321234567890
    # n = 1111111111111
    # n = 1234567890123
    n = 1001000100100111
    n = 8769
    # n = 1

    print n

    print "-" * 50
    print int2word(n)
    print "-" * 50

def get_digit(num, index):
    modulo = pow(10, index+1)
    div = pow(10, index)
    return (num%modulo)//div
for i in range(4):
    print "{} th index of number {} is {}".format(i, 1234, get_digit(1234, i))
