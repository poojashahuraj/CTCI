
"""
In dynamic programming we store answers to subproblems in an array. and compute rest elements of an arrya using that matrix.
space complexity o(mn) and time complexicity also o(mn) i think
"""


def longest_common_substring(s1, s2):
    m = [[0 for j in range(len(s2)+1)] for i in range(len(s1)+1)]
    longest, x_longest = 0, 0

    for x in xrange(1, 1 + len(s1)):
        for y in xrange(1, 1 + len(s2)):
            if s1[x - 1] == s2[y - 1]:
                m[x][y] = m[x - 1][y - 1] + 1
                if m[x][y] > longest:
                    longest = m[x][y]
                    x_longest = x
            else:
                m[x][y] = 0
    return s1[x_longest - longest: x_longest]

print longest_common_substring("makPoojashahurajnikar", "karPoojashahuraj")