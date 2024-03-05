class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMax = []
        leftMax.append(height[0])
        rightmax = []
        rightmax.append(height[-1])
        for i in range(1 , n):
            leftMax.append(max(leftMax[-1], height[i]))  

        for i in range(n - 2 , -1 ,-1):
            rightmax.append(max(rightmax[-1], height[i]))  
        rightmax.reverse()                  
        vol = 0
        for i in range(n):
            k = min(leftMax[i], rightmax[i]) - height[i]
            vol += k
        return vol    
