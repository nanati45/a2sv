class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        max_length = 0
        min_queue = deque()
        max_queue = deque()

        left = right = 0

        while right < len(nums):
            while min_queue and nums[right] < min_queue[-1]:
                min_queue.pop()
            
            while max_queue and nums[right] > max_queue[-1]:
                max_queue.pop()
            
            min_queue.append(nums[right])
            max_queue.append(nums[right])

            while max_queue[0] - min_queue[0] > limit:
                if nums[left] == min_queue[0]:
                    min_queue.popleft()
                if nums[left] == max_queue[0]:
                    max_queue.popleft()
                left += 1
            
            max_length = max(max_length, right - left + 1)
            right += 1
        
        return max_length