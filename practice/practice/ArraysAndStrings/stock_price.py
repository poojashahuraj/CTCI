import sys


def max_profit_stock(ip_arr):
    max_profit = -sys.maxint - 1
    min_buy_price = ip_arr[0]
    for i in ip_arr:
        if i < min_buy_price:
            min_buy_price = i
        potential_profit = i - min_buy_price
        max_profit = max(max_profit, potential_profit)
    return max_profit


print max_profit_stock([11, 3, 2, 1, 14, 6, 12])


def get_max_profit(ip_arr):
    min_buy_price = sys.maxint
    max_profit = -sys.maxint - 1
    for i in ip_arr:
        if i < min_buy_price:
            min_buy_price = i
        potential_profit = i - min_buy_price
        max_profit = max(potential_profit, max_profit)
    return max_profit, min_buy_price


print get_max_profit([11, 3, -2, 1, 14, 6, 12])
