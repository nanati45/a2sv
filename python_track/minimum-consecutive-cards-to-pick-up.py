class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        indexes = {}
        lengMin = 10**6

        for i in range(len(cards)):
            if cards[i] in indexes:
                lengMin = min(lengMin,i-indexes[cards[i]]+1)
            indexes[cards[i]] = i

        if lengMin == 10**6:
            return -1

        return lengMin

                     

                
                 