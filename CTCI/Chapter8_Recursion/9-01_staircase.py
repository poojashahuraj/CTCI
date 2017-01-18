"""
# 9.1. A child is running up a staircase with n steps, and can hop either 1
# step, 2 steps, or 3 steps at a time. Implement a method to count how many
# possible ways the child can run up the stairs.
"""

def hop_staircase(n):
    if n < 0:
        raise ValueError
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        count = hop_staircase(n-1)+hop_staircase(n-2)+hop_staircase(n-3)
        return count

def fibbo(n):
    if n < 0:
        return -1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        n = fibbo(n-1)+fibbo(n-2)
        return n
op = []
for i in range(6):
    op.append(fibbo(i))

print "Fibbo series", op
print "Hop stair case:", hop_staircase(5)

def staircase(num_stairs):
    n = num_stairs - 2
    for stairs in range(1, num_stairs):
        print ' ' * n, '#' * stairs
        n -= 1
    print '#' * num_stairs
staircase(6)