# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/submissions/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit

"""
I TARBERUTYUN NUYNI ARAJINI
AYSTEX KAROX ENQ GNEL EV VACHAREL MI QANI ANGAM
AYSINQN AMEN NAGAM ERB PROFIT KA KAROX ENQ ANEL
"""