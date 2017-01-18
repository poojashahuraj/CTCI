input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
"""
dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
"""

def lengthLongestPath(ip):
    maxlen = 0
    pathlen = {0: 0}
    p = ip.splitlines()
    for line in p:
        name = line.lstrip('\t')
        depth = len(line) - len(name)
        if '.' in name:
            maxlen = max(maxlen, pathlen[depth] + len(name))
        else:
            pathlen[depth + 1] = pathlen[depth] + len(name) + 1
        print "name: {}, pathlen:{}".format(name, pathlen)
    return maxlen

print lengthLongestPath(input)


dict_a = {}
dict_a[0] = "zero"
dict_a["p"] = "pooja"
print dict_a[0]
print dict_a["p"]