class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        windows = []
        left = 0
        right = len(cardPoints) - 1
        maxSum = 0
        
        leftSum = [0] * (k+1)
        for i in range(1,k+1):
            leftSum[i] = cardPoints[i-1] + leftSum[i-1]

        rightSum = [0] * (k+1)
        revCard = cardPoints[::-1]

        for i in range(1,k+1):
            rightSum[i] = revCard[i-1] + rightSum[i-1]
        
        total = []
        r = k 
        for i in range(k+1):
            total.append(leftSum[i] + rightSum[r])
            r -=1

        return max(total)
            