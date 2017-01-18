"""
Write a method which returns all subsets of a set. this is also called as power set
say ip = [1,2,3]
op = [[], [1],[2],[3],[1,2],[2,3],[1,3],[1,2,3]]
See power set of empty set will have one value, that is empty set.
"""
def list_powerset(lst):
    # the power set of the empty set has one element, the empty set
    result = [[]]
    for x in lst:
        # for every additional element in our set
        # the power set consists of the subsets that don't
        # contain this element (just take the previous power set)
        # plus the subsets that do contain the element (use list
        # comprehension to add [x] onto everything in the
        # previous power set)
        result.extend([subset + [x] for subset in result])
    return result

print list_powerset([1,2,3])
print list_powerset([1,2,2])