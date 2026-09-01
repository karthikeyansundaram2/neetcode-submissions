class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minNum=prices[0]
        profit=0
        bestProfit=0
        for i in range(1,len(prices)):
            if(prices[i]>minNum):
                profit=prices[i]-minNum
                bestProfit=max(bestProfit,profit)
            elif prices[i]<minNum:
                minNum=prices[i]
        
        return bestProfit
        