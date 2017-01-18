ones = ["", "one ", "two ", "three ", "four ", "five ",
        "six ", "seven ", "eight ", "nine "]

tens = ["ten ", "eleven ", "twelve ", "thirteen ", "fourteen ",
        "fifteen ", "sixteen ", "seventeen ", "eighteen ", "nineteen "]

twenties = ["", "", "twenty ", "thirty ", "forty ",
            "fifty ", "sixty ", "seventy ", "eighty ", "ninety "]

thousands = ["", "thousand ", "million ", "billion"]


def int2word(n):
    n3 = []
    r1 = ""
    ns = str(n)
    for k in range(3, 33, 3):
        r = ns[-k:]
        q = len(ns) - k
        if q < -2:
            break
        else:
            if q >= 0:
                n3.append(int(r[:3]))
            elif q >= -1:
                n3.append(int(r[:2]))
            elif q >= -2:
                n3.append(int(r[:1]))
        r1 = r
    nw = ""
    for i, x in enumerate(n3):
        b1 = x % 10
        b2 = (x % 100) // 10
        b3 = (x % 1000) // 100
        # print b1, b2, b3  # test
        if x == 0:
            continue  # skip
        else:
            t = thousands[i]
        if b2 == 0:
            nw = ones[b1] + t + nw
        elif b2 == 1:
            nw = tens[b1] + t + nw
        elif b2 > 1:
            nw = twenties[b2] + ones[b1] + t + nw
        if b3 > 0:
            nw = ones[b3] + "hundred " + nw
    return nw


if __name__ == '__main__':
    # select an integer number n for testing or get it from user input
    # n = 4321234567890
    # n = 1111111111111
    # n = 1234567890123
    n = 10010
    # n = 1

    print n

    print "-" * 50
    print int2word(n)
    print "-" * 50