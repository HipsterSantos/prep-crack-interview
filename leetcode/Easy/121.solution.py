class Solution:
    prices = 0
    def __init__(self):
        pass
    def selStock(self,prices:List[int]):
        for index, value in enumerate(prices):
            self.prices += val - prices[index+1]
