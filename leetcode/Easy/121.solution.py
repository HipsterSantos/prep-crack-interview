class Solution:
    prices = 0
    def __init__(self):
        pass
    def selStock(self,prices:List[int]):
        for index, value in enumerate(prices):
            self.prices += val - prices[index+1]

    def buyStock(self, prices:List[int]):
        moving  = True
        profit =  list()
        while(moving):
            for ind, val in enumerate(prices):
                for a in range(ind+1,(len(prices) )-1 ):
                    profit.add(prices[a] - val)
                    if(a == len(prices)):
                        moving = False
                return profit



class JewelAndStone:
    def solution(j):
        s = "aAAbbbb"
        for ind,val in enumerate(jsd)  :
            for 