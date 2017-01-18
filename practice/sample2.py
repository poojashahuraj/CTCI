class RemoveChar(object):
    def __init__(self, input_str, char):
        self._input_str_remove = input_str
        self._char = char
        pass

    def remove_char(self):
        new_arr = list(self._input_str_remove)
        print new_arr
        new_arr.remove(self._char)
        rt = ''
        for i in new_arr:
            rt = rt + i
        return rt
rc = RemoveChar("abc", "b")
print rc.remove_char()

