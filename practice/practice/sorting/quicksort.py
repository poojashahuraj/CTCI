def quick_sort(l):
    if len(l) <= 1:
        return l
    else:
        pivot = l[0]
        smaller_than_pivot = [i for i in l[1:] if i <= pivot]
        larger_than_pivot = [i for i in l[1:] if i > pivot]
        op = quick_sort(smaller_than_pivot) + [pivot] + quick_sort(larger_than_pivot)
        return op

print quick_sort([3, 2, 6, 1, 8, 3, 5, 2, 8, 22, 11])
