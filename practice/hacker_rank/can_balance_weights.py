

def subset_sum(numbers, target, partial=None):
    if partial is None:
        partial = []
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target:
        print "sum(%s)=%s" % (partial, target)
    if s >= target:
        return  # if we reach the number why bother to continue

    for index, value in enumerate(numbers):
        n = value
        remaining = numbers[index+1:]
        subset_sum(remaining, target, partial + [n])


if __name__ == "__main__":
    subset_sum([3, 9, 8, 4, 5, 7, 10], 15)
