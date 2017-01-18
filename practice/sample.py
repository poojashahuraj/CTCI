# coding=utf-8
import unittest


# from algorithms import sorting




class BubbleSort(object):
    """
    Approach:
    Bubblesort is an elementary sorting algorithm. The idea is to
    imagine bubbling the smallest elements of a (vertical) array to the
    top; then bubble the next smallest; then so on until the entire
    array is sorted. Bubble sort is worse than both insertion sort and
    selection sort. It moves elements as many times as insertion sort
    (bad) and it takes as long as selection sort (bad). On the positive
    side, bubble sort is easy to understand. Also there are highly
    improved variants of bubble sort.
    """

    def __init__(self, input_arr):
        self._input_arr = input_arr

    def bubble_sort(self):
        """
        :param input_arr: Array of elements we want to sort
        :return: sorted array
        a = [9,8,7,6,5,4,3,2,1,0]
        ans = [0,1,2,3,4,5,6,7,8,9]
        Two cascaded for loops so
        Time Complexity:
        Best O(n^2); Average O(n^2); Worst O(n^2).
        """
        for i in range(len(self._input_arr)):
            for j in range(len(self._input_arr) - 1, i, -1):
                if self._input_arr[i] > self._input_arr[j]:
                    self._input_arr = self.swap(i, j, self._input_arr)
                    # print self._input_arr
        return self._input_arr

    def swap(self, i, j, input_arr):
        tmp = input_arr[i]
        input_arr[i] = input_arr[j]
        input_arr[j] = tmp
        return input_arr


print BubbleSort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]).bubble_sort()
print BubbleSort([8, 5, 3, 1, 9, 6, 0, 7, 4, 2, 5]).bubble_sort()



# Write a method which will remove any given character from a String
def sample1(char, string):
    import re
    return re.sub(char, "*", string)


print sample1('o', "pooja")


class Permutations(object):
    def __init__(self, str):
        self._string_ = str

    def run(self):
        if len(self._string_) == 0:
            return []
        if len(self._string_) == 1:
            return self._string_
        lst = list(self._string_)
        l = ''
        l_ret = []
        for i in range(len(lst)):
            first_char = lst[i]
            remaining_list = lst[:i] + lst[i + 1:]
            for p in Permutations(remaining_list).run():
                l = first_char + p
                l_ret.append(l)
        return l_ret


# remove removes the first matching value, not a specific index:
# del removes a specific index:
# and pop returns the removed element:
p = Permutations("abc")
print p.run()

string = "maknikar"
print "Pick last element of given string {} with -1 index.{}".format(string, list(string)[-1])


def extendList(val, lst=[]):
    lst.append(val)
    return lst


def extend_list(val, lst=None):
    if lst is None:
        lst = []
    lst.append(val)
    return lst


def multipliers():
    return [lambda x: i * x for i in range(4)]


print multipliers()
print [m(2) for m in multipliers()]


class Parent(object):
    x = 1


class Child1(Parent):
    pass


class Child2(Parent):
    pass


print Parent.x, Child1.x, Child2.x
Child1.x = 2
print Parent.x, Child1.x, Child2.x
Parent.x = 3
print Parent.x, Child1.x, Child2.x

list = [[]] * 5
print list  # [[], [], [], [], []]
list[0].append(10)
print list  # [[10], [10], [10], [10], [10]]
list[1].append(20)
print list  # [[10, 20], [10, 20], [10, 20], [10, 20], [10, 20]]
list.append(30)
print list  # [[10, 20], [10, 20], [10, 20], [10, 20], [10, 20], 30]

def abc(lst):
    for i, v in enumerate(lst):
        if i % 2 == 0 and v % 2 == 0:
            print v
lst_1 = [1, 3, 5, 8, 10, 13, 18, 36, 78]
lst_2 = [i for i in xrange(5)]
abc(lst_1)
abc(lst_2)


# Write a method which will remove any given character from a String? (solution)
class RemoveChar(object):
    def __init__(self, input_str, char):
        self._input_str_remove = input_str
        self._char = char
        pass

    def remove_char(self):
        new_arr = list(self._input_str_remove)
        new_arr.delete(self._char)
        print a

rc = RemoveChar("abc", "b")
print rc.remove_char()
"""
For performance, especially when you're iterating over a large range, xrange() is usually better.
range creates a list, so if you do range(1, 10000000) it creates a list in memory with 9999999 elements.
xrange is a sequence object that evaluates lazily.
"""
"""
5 / 2 will return 2.5 and 5 // 2 will return 2 .
The former is floating point division, and the latter is floor division, sometimes also called integer division.
Regardless of the future import, 5.0 // 2 will return 2.0 since that's the floor division result of the operation

Flask is a “microframework” primarily build for a small application with simpler requirements.
In flask, you have to use external libraries.  Flask is ready to use.
Pyramid are build for larger applications.
It provides flexibility and lets the developer use the right tools for their project.
The developer can choose the database, URL structure, templating style and more. Pyramid is heavy configurable.
Like Pyramid, Django can also used for larger applications.  It includes an ORM.
"""
