# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
def buy_sell_stock(prices):
    left, right = 0, 1
    profit = 0
    while right < len(prices):
        if prices[right] > prices[left]:
            profit = max(profit, prices[right] - prices[left])
        else:
            left = right
        right += 1
    return profit

prices = [7,1,5,3,6,4]


print(buy_sell_stock(prices))
"""
VERCNENQ 2 POINTER
LEFT = 0 RIGHT = 1
AYSINQN ENTADRUM ENQ GNEL ENQ 0 RD ORY VACHAREL 1 RD ORY
BAYC VACHARUM ENQ MIAYN AYN DEPQUM ETE AYD ORVA GINY AVELI BARDZR E QAN AYSORVANY
HAKARAK DEPQUM NSHANAKUM E VOR KA AVELI LAV OR VOR KARELI E GNEL AYN
AYSINQN LEFT = RIGHT => NOR GNELU OR VOR POTENCIAL KAROX E AVELI LAVY LINEL
"""