from collections import defaultdict
def stock_profit(ip):
    op = defaultdict(int)
    for i in range(len(ip)):
        temp =[]
        for j in range(i+1, len(ip)):
            temp.append(ip[j]-ip[i])
        if temp:
            op[i] = max(temp)
    print op.values().index(max(op.values()))
# time complexity of above problem is o(n2), consider two consecutive for loops.


def stock_profit_2(ip):
    cheapest = ip[0]
    max_profit = 0
    for i in range(1, len(ip)):
        cheapest = min(cheapest, ip[i])
        max_profit = max(max_profit, ip[i]-cheapest)
    print max_profit, cheapest

stock_profit([6, 4, 2, 6, 8, 7, 9])
stock_profit_2([6, 4, 2, 6, 8, 7, 9])