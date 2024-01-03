class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        ans=[]
        res=[]
        leng=len(nums)+1
        zeroes=[0]*leng
        ones=[0]*leng
        for i in range(1,len(nums)+1):
            if nums[i-1]==0:
                zeroes[i]=zeroes[i-1]+1
            else:
                zeroes[i] =zeroes[i-1]   
        n=nums[::-1]        
        for i in range(1,len(n)+1):
            if n[i-1]==1:
                ones[i]=ones[i-1]+1 
            else:
                ones[i] =ones[i-1]     
        ones=ones[::-1]  
        for i in range(leng):
            ans.append(zeroes[i]+ones[i])
        mx=max(ans)
        for i in range(leng):
            if ans[i]==mx:
                res.append(i)

        return res           
