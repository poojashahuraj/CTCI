def recursive_fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    elif n > 1:
        c = recursive_fibo(n - 1) + recursive_fibo(n - 2)
        return c
    else:
        return -1


op = []
for i in range(10):
    op.append(recursive_fibo(i))
print "Recursive fibbo series {}".format(op)


def iterative_fibo(n):
    if n < 0:
        return -1
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        a = 0
        b = 1
        c = a+b
        for i in range(n-1):
            c = a + b
            a = b
            b = c
        return c
op = []
for i in range(10):
    op.append(iterative_fibo(i))
print "Iterative fibbo series:{}".format(op)
