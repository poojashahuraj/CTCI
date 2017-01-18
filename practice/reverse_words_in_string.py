class ReverseWords(object):
    def __init__(self):
        pass

    def reverse_words_in_string(self, input_string):
        arr = input_string.split(" ")
        re_val = ''
        for i in arr:
            re_val = re_val + self.reverse(i)+" "
        print re_val

    @staticmethod
    def reverse(word):
        return word[::-1]

r = ReverseWords()
r.reverse_words_in_string("I am pooja maknikar")