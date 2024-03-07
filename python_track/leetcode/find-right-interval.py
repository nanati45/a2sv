class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        store = {}
        for i in range(len(intervals)):
            store[intervals[i][0]] = i
        key_list = list(store.keys())
        key_list.sort()
        def checker(num) :
            l = 0 
            r = len(intervals) - 1
            res = 0
            while l <= r :
                mid = l + (r - l) // 2
                if key_list[mid] >= num:
                   res = key_list[mid]
                   r = mid - 1
                else:
                    l = mid + 1 
            return store[res] if l < len(key_list) else -1         
        ans = []
        for i in intervals:
            ans.append(checker(i[1]))
        return ans   

