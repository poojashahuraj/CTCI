# coding=utf-8
"""
Given a string of opening and closing parentheses, check whether it’s balanced.
"""

def printParam(toOpen, toClose, currString):
    if toOpen == toClose == 0:
        print currString
        return
    if toOpen > 0:
        printParam(toOpen -1, toClose, currString + "(")
    if toClose > toOpen:
        printParam(toOpen, toClose-1, currString + ")")


def validate_str(ip_str):
    dict_a = {"[": "]", "{": "}", "(": ")"}
    stack = []

    for i, v in enumerate(ip_str):
        if v in dict_a.keys():
            stack.append(v)
        elif v in dict_a.values():
            if len(stack) == 0:
                return False
            last_open = stack.pop()
            if dict_a[last_open] != v:
                return False
    # this covers this case where open brackets are closed
    return len(stack) == 0


if __name__ == "__main__":
    failed_ip = ["{a[b(c)d]", "{a[b(c]d)e}", "}ip{lk[p]"]
    for i in failed_ip:
        assert validate_str(i) == False
    assert validate_str("Pooja(ma)k{n}i[ka]") is True
    printParam(3, 3, '')
    print "----------------------"
    printParam(2,2,'')


def valid_parenthesis(opening, closing, op):
    if opening == closing == 0:
        print op
    if opening > 0:
        valid_parenthesis(opening-1, closing, op+"(")
    if closing > opening:
        valid_parenthesis(opening, closing-1, op+")")
valid_parenthesis(3,3,"")