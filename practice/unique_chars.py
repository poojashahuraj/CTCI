def unique_chars_str(string):
    unique = list(set(list(string)))
    all_chars = list(string)
    if len(unique) == len(all_chars):
        print "OK: '{}' has all unique characters.".format(string)
    else:
        print "NO: {} does not have all unique characters.".format(string)

unique_chars_str("Pooja")
unique_chars_str("abcd")
unique_chars_str("qwertyu")
unique_chars_str("formation data systems")