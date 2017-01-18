"""
Given an expression validate string if all the open arenthesis are closed.
"""
from unittest import TestCase

dict_a = {"[": "]", "{": "}", "(": ")"}


def validate_ip(ip):
    stack = []
    for index, value in enumerate(ip):
        if value in dict_a.keys():
            # this means we found opening bracket.
            stack.append(value)
        elif value in dict_a.values():
            # this means we found closing bracket
            if len(stack) == 0:
                # because we already got closing bracket and no opening brackets were stored.
                return False
            last_opening_bracket = stack.pop()
            if dict_a[last_opening_bracket] != value:
                return False
        else:
            # random chars
            pass
    return len(stack) == 0


class ValidationTest(TestCase):
    def test_validation(self):
        fail_cases = ["j[a]v{a", "j]a[va(i)", "foo{[}pa]nda"]
        for i in fail_cases:
            assert validate_ip(i) is False
        assert validate_ip("poo(o)jafo{o[b(a)r]panda}") is True
