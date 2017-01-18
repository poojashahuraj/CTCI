def is_good_build(build):
    # lets assume even number is good build and odd number is bad build
    if build % 2 == 0:
        return True
    else:
        return False


def get_all_builds(start_date, end_date):
    return [2, 4, 6, 8, 10, 11, 15, 17, 19,21]


def first_bad_build(builds):
    if not builds:
        return []
    if len(builds) == 1:
        if is_good_build(builds[0]):
            return [-1]
        else:
            print builds[0]
            return builds[0]
    mid_index = len(builds)/2
    mid_build = builds[mid_index]
    if is_good_build(mid_build):
        first_bad_build(builds[mid_index+1:])
    else:
        print mid_build,
        first_bad_build(builds[:mid_index])
    return


builds = get_all_builds("start_date", "end_date")
first_bad_build([2, 4, 6, 8, 10, 14, 16, 11, 15, 17, 19, 21]) # prints 17,15,11
print "----------------------------"
first_bad_build([2, 4, 6, 7])#prints 7
