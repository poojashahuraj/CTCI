"""
# 9.8. Given an infinite number of quarters (25 cents), dimes (10 cents),
# nickels (5 cents) and pennies (1 cent), write code to calculate the
# number of ways of representing n cents.
Lets divide the problem:
first let's start with 25 cents
100 = ways(100, other)+ ways(75, other) + ways(50, other)+ ways(25, other)+ ways(0)4 quaters
"""

def max_coins(amt, coin_val):
    return amt//coin_val

dict_a = {25:10, 10:5, 5:1}

def change_making(total_amt, coin_val):
    if coin_val == 1:
        return 1
    ways = 0
    for i in range(max_coins(total_amt, coin_val)+1):
        next_denom = dict_a[coin_val]
        remaining = total_amt - (i*coin_val)
        ways += change_making(remaining, next_denom)
    return ways

print change_making(6, 25)






















"""
lets think of this as recursive problem. method change_count(100)
say n =100
so  change_count(100 using 0 quarters)+ change_count(100 using 1 quarter)
    +change_count(100 using 2 quarters)+ change_count(100 using 3 quarter)
    +change_count(100 using 4 quarters)
"""
dict_b = {25:10, 10:5, 5:1}

def get_max(sum_val, coin_val):
    return sum_val//coin_val + 1

def make_change(sum_val, coin_val=25):
    if coin_val == 1:
        return 1
    ways = 0
    for i in range(get_max(sum_val, coin_val)):
        remaining_amt = sum_val - i*coin_val
        ways += make_change(remaining_amt, dict_b[coin_val])
    return ways

print make_change(6)