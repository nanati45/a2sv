class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans=0
        for i in range(len(points)-1):
            n=abs(points[i][0]-points[i+1][0])
            n2=abs(points[i][1]-points[i+1][1])
            ans+=max(n,n2)
        return ans    

