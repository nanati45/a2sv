class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        s = 0
        while target > 1 :
            while maxDoubles and target> 1 :
                if target % 2 != 0 :  
                    s += 1
                target = target // 2
                maxDoubles -= 1
                s += 1
            s += (target - 1)
            target -= (target - 1)

        return s        