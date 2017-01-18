def valid_parenthesis(ip_str):
    dict_a = {"{":"}", "(":")", "[":"]"}
    stack = []
    for index, value in enumerate(ip_str):
        if value in dict_a.keys():
            stack.append(value)
        elif value in dict_a.values():
            if len(stack) == 0:
                return False
            last_open = stack.pop()
            if dict_a[last_open] != value:
                return False
    return len(stack) == 0

print valid_parenthesis("{p[o]m}(a)")
print valid_parenthesis("{p[o]m}a)")
print valid_parenthesis("{p[o]m(}a)")
