"""
Given infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents), and pennies (1 cents),
calculate the number of ways of representing n cents.

"""
dict_a = {25:10, 10:5, 5:1}


def max_count(sum_val, coin_val):
    return sum_val//coin_val +1


def make_change(sum_val, coin_val=25):
    if coin_val == 1:
        return 1
    max_c = max_count(sum_val, coin_val)
    ways = 0
    for i in range(max_c):
        remain_val = sum_val - i*coin_val
        ways += make_change(remain_val, dict_a[coin_val])
    return ways

print make_change(6)
