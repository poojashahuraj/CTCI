def perm(ip_str):
    if len(ip_str) == 1:
        return [ip_str]
    else:
        result = []
        for i, v in enumerate(ip_str):
            result += [v+p for p in perm(ip_str[:i]+ip_str[i+1:])]
        return result

print perm("abc")