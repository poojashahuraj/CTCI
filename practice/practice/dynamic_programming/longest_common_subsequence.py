# coding=utf-8
"""
LCS Problem Statement: Given two sequences, find the length of longest sub sequence present in both of them.
A sub sequence is a sequence that appears in the same relative order, but not necessarily contiguous.
For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are sub sequences of “abcdefg”.
So a string of length n has 2^n different possible sub sequences.
"""


def longest_common_subsequence(s1, s2, m, n):
    if m == 0 or n == 0:
        return 0
    elif s1[m - 1] == s2[n - 1]:
        return 1 + longest_common_subsequence(s1, s2, m - 1, n - 1)
    else:
        return max(longest_common_subsequence(s1, s2, m, n - 1), longest_common_subsequence(X, Y, m - 1, n))

# Time complexity of this solution is 2 to the power n.


# Dynamic programming approach will improve time complexcity to O(mn), we fill up array bottom up.
def lcs(mat_1, mat_2):
    # find the length of the strings
    m = len(mat_1)
    n = len(mat_2)

    # declaring the array for storing the dp values
    dp_mat = [[None] * (n + 1) for i in xrange(m + 1)]

    """Following steps build L[m+1][n+1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]"""
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp_mat[i][j] = 0
            elif mat_1[i - 1] == mat_2[j - 1]:
                dp_mat[i][j] = dp_mat[i - 1][j - 1] + 1
            else:
                dp_mat[i][j] = max(dp_mat[i - 1][j], dp_mat[i][j - 1])

    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return dp_mat[m][n]


# end of function lcs


# Driver program to test the above function
X = "AGGTAB"
Y = "GXTXAYB"
print "Length of LCS is ", lcs(X, Y)