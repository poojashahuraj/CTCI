from compiler.misc import Stack


def reverse_a_string(ip):
    ip_arr = ip.split(" ")
    op = ""
    for i in range(len(ip_arr)-1, -1, -1):
        op += ip_arr[i]
        if i is not 0:
            op += " "
    return op
print reverse_a_string("this is practice")


# get valid parenthesis
def valid_parenthesis(opening, closing, op):
    if opening == closing ==0:
        print op
    if opening > 0:
        valid_parenthesis(opening-1, closing, op+"(")
    if closing > opening:
        valid_parenthesis(opening, closing-1, op+")")

print valid_parenthesis(3,3, "")


# check string has valid parenthesis
def valid_parenthesis_str(input_string):
    dict_a = {"(":")", "{":"}", "[":"]"}
    stack_a = []
    for index, value in enumerate(input_string):
        if value in dict_a.keys():
            stack_a.append(value)
        elif value in dict_a.values():
            if len(stack_a) == 0:
                return False
            last_opened = stack_a.pop()
            if dict_a[last_opened] != value:
                return False

    return len(stack_a) == 0

print valid_parenthesis_str("poo(ja)[makni]kar{is}")
print valid_parenthesis_str("poo(ja)[makni{]is}")

def check_if_two_strings_are_anagrams(ip_one, ip_two):
    if len(ip_two) == len(ip_one):
        return
    sorted(ip_one)
    sorted(ip_two)
    op = Stack()