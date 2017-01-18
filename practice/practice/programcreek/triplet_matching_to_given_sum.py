"""
Find a triplet from a given array which matches the sum
"""


def find_triplet(ip_arr, given_sum):
    # lets just sort the array first
    ip_arr = sorted(ip_arr)
    for i in range(len(ip_arr)-2):
        j = i+1
        k = len(ip_arr)-1
        while j < k:
            s = ip_arr[i] + ip_arr[j] + ip_arr[k]
            if s == given_sum:
                return ip_arr[i], ip_arr[j], ip_arr[k]
            elif s > given_sum:
                k -= 1
            elif s < given_sum:
                j += 1
    return -1
# for sorting the given array we invested o(nlogn)
# then for finding the triplet we got o(n^2)
# o(n^2)+nlogn
print find_triplet([12, 3, 4, 1, 6, 9], 24)
