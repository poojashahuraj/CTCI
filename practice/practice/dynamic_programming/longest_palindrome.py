def longest_pali(ip_str):
    op = []
    for index, value in enumerate(ip_str):
        s = ""
        for j in range(index, len(ip_str)):
            s += ip_str[j]
            if is_palin(s):
                op.append(s)
    return max(op, key=len)


def is_palin(ip_str):
    return ip_str == ip_str[::-1]

print longest_pali("maknipoojaajoopmakni")