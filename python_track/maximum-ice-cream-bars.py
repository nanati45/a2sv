class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        counter = 0 
        for i in range(len(costs)):
            coins -= costs[i]
            if coins < 0:
                break
            counter +=1
        return counter        