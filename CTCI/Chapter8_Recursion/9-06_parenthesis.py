"""
# 9.6. Implement an algorithm to print all valid (e.g., properly opened and
# closed) combinations of n-pairs of parentheses.
"""


def parenthesis_method(opening, closing, op):
    if opening == closing == 0:
        print op
        return
    if opening > 0:
        parenthesis_method(opening-1, closing, op=op + "(")
    if closing > opening:
        parenthesis_method(opening, closing-1, op=op + ")")
    return op

parenthesis_method(3, 3, "")
