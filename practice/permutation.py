class Permutation(object):
    def __init__(self):
        pass

    def perm(self, n):
        if len(n) == 1:
            return [n]
        result = []
        for idx, val in enumerate(n):
            result += [val + p for p in self.perm(n[:idx] + n[idx + 1:])]
        return result


p = Permutation()
print p.perm("abc")
print p.perm("123")
