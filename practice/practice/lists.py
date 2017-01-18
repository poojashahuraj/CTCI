# Python program to find if there are two elements wtih given sum

## SOLUTION 1 ##
CONST_MAX = 100000

# function to check for the given sum in the array
def printPairs(arr, arr_size, sum):
    # initialize hash map as 0
    binmap = [0] * CONST_MAX

    for i in range(0, arr_size):
        temp = sum - arr[i]
        if (temp >= 0 and binmap[temp] == 1):
            print "Pair with the given sum is", arr[i], "and", temp
        binmap[arr[i]] = 1


# driver program to check the above function
A = [1, 4, 45, 6, 10, -8]
n = 16
printPairs(A, len(A), n)

## SOLUTION 1 ##
# Sort the array, have two indices one at the start and one and then end, say p1 and p2.
# sum =p1+p2, if sum is less than given then increment p1 if sum is less than given then decrement p2

def find_two_numbers(arr, sum):
    p1 = 0
    p2 = len(arr)-1
    arr = sorted(arr)
    l = len(arr)
    while p1 < l and p2 > 0:
        temp = arr[p1] +arr[p2]
        if sum == temp:
            print "{} = arr[{}] + arr[{}] = {} + {}".format(sum, p1, p2, arr[p1],arr[p2])
            break
        elif temp > sum:
            p2 -= 1
        else:
            p1 += 1
    return p1, p2

print find_two_numbers(A, 16)