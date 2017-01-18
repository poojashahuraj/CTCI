def perm(ip_str):
    if len(ip_str) == 1:
        return [ip_str]
    result = []
    for i, v in enumerate(ip_str):
        remaining_str = ip_str[0:i]+ip_str[i+1:]
        result.extend([v+i for i in perm(remaining_str)])
    return result

print perm("ABC")

def premu(ip):
    if len(ip) == 1:
        return [ip]
    result = []
    for idx, value in enumerate(ip):
        remaining_str = ip[:idx]+ip[idx+1:]
        result.extend([value+p for p in premu(remaining_str)])
    return result
print premu("ABC")