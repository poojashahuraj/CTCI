def replace_spaces_in_str(string):
    return string.replace(" ", "%20")

for i in ["pooja maknikar", "formation data systems"]:
    print "<{}> after replacing space is <{}>.".format(i, replace_spaces_in_str(i))
