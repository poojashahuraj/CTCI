class Palindrome(object):
    def __init__(self):
        pass

    def is_palindrome(self, ip):
        if str(ip) == str(ip)[::-1]:
            return True
        else:
            return False

    def longest_palindrome(self, ip):
        l = len(ip)
        ret_list = []
        for i in range(l):
            s =""
            for j in range(i, l):
                s += ip[j]
                if self.is_palindrome(s):
                    ret_list.append(s)
        print ret_list
        return max(ret_list, key=len)
p = Palindrome()
#print p.longest_palindrome("i like racecars")
print p.longest_palindrome("abcddcba")
