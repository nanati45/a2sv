class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
            max_=sum(nums[:k])
            avg=max_/k
            max_avg=avg
            l=0
            for r in range(k,len(nums)):
                max_=max_+ nums[r]-nums[l]
                new_avg=max_/k
                max_avg=max(max_avg,new_avg)
                l+=1
            return (max_avg)

        