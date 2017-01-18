def fibbo_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n < 0:
        return -1
    else:
        ans = fibbo_recursive(n-1)+fibbo_recursive(n-2)
    return ans

result = []
for i in range(10):
    result.append(fibbo_recursive(i))
print result


def fibbo_iterative(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a = 1
    b = 1
    for i in range(3,n+1):
        c = a + b
        a = b
        b = c
    return b

result = []
for i in range(10):
    result.append(fibbo_iterative(i))
print result
