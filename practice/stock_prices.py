"""
stock_prices_yesterday = [10, 7, 12, 5, 8, 11, 4, 9]
indices indicate time is increasing. index 0 means say at time 10am, then index 1 means after 10am.
Point is your buying price 5 and selling price 12 is not possible becasue u can not sell before buying.

# returns 6 (buying for $5 and selling for $11)
"""


class StockPrices(object):
    def __init__(self, ip):
        self._ip = ip

    def run(self):
        if len(self._ip) < 2:
            raise ValueError("minimum two values are required.")
        min_sell_price = self._ip[0]
        max_profit = self._ip[1]-self._ip[0]
        for i in range(1, len(self._ip)):
            buy_price = self._ip[i]
            for j in range(i + 1, len(self._ip)):
                potential_profit = self._ip[j] - buy_price
                min_sell_price = min(min_sell_price, buy_price)
                max_profit = max(potential_profit, max_profit)
        print "Maximum profit:{}".format(max_profit),
        print "Minimum sell price:{}".format(min_sell_price)


s = StockPrices([10, 7, 13, 5, 8, 11, 9])
s.run()
