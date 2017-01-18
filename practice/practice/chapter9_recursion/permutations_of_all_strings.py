"""
Write a program to return all permutations of strings.
"""
def manual_perm(ip_str):
    if len(ip_str) == 1:
        return [ip_str]

    result = []
    for idx, value in enumerate(ip_str):
        result.extend([value + perm for perm in manual_perm(ip_str[0:idx]+ip_str[idx+1:])])
    return result


def perm_len(iterable, r=None):
    # perm_len('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # perm_len(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = range(n)
    cycles = range(n, n-r, -1)
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

print manual_perm("ABC")
for i in perm_len("ABC", 2):
    print i
