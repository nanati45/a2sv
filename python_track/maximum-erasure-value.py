class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        n = len(nums)
        maxSum = 0
        counter = defaultdict(int)

        currSum = 0
        while right < n:
            if counter[nums[right]] > 0:
                counter[nums[left]] -=1
                currSum -= nums[left]
                left +=1
            else:
                counter[nums[right]] +=1
                currSum += nums[right]
                right +=1

            maxSum = max(maxSum , currSum)  

        return maxSum      

                



