class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse=True)
        processorTime.sort()

        index = 0
        i = 0
        ans = []
        while index < len(tasks):
            ans.append(tasks[index] + processorTime[i])
            index += 4
            i += 1
        return max(ans)