def reverse_a_string_wth_stack(ip_str):
    stack = []
    for not_use, val in enumerate(ip_str):
        stack.append(val)
    op = ""
    while stack:
        op += stack.pop()
    return op
print reverse_a_string_wth_stack("pooja")