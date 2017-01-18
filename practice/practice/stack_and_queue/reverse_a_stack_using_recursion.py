"sort the stack using recursion"


def sort_stack(ip_stack):
    if not ip_stack:
        return None
    while ip_stack:
        t = ip_stack.pop()
        sort_stack(ip_stack)
        print insert_in_stack(ip_stack, t)
    return ip_stack


def insert_in_stack(stack_ip, val):
    if not stack_ip:
        return [val]
    if val > stack_ip[-1]:
        # means value is greater than top element of the stack then just put value at top of stack.
        return stack_ip.append(val)
    else:
        t = stack_ip.pop()
        # pop the element and recursively call insert method.
        insert_in_stack(stack_ip, val)
        stack_ip.append(t)
    return stack_ip

print sort_stack([1, 4, 3, 5, 7, 2])