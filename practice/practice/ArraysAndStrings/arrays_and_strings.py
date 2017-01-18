# coding=utf-8
"""
Write a method to replace all spaces in a string with ‘%20’.
"""


def replace_all(ip):
    arr = ip.split(' ')
    op = ""
    for i in range(len(arr)-1):
        op += arr[i]+"%20"
    op = op + arr[len(arr)-1]
    return op
print replace_all("colorado state university")