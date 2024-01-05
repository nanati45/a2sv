class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False

        mx= max(arr)
        idx= arr.index(mx)
        if idx == len(arr)-1 or idx == 0:
            return False

        stack=[]
        for i in range(1,len(arr)):
            if i <= idx and arr[i-1]< arr[i]:
                stack.append(arr[i])
            elif i > idx and arr[i-1] > arr[i]:
                stack.append(arr[i])
            else:
                return False
        return True            
