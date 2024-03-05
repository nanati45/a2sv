class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = []
        for i in costs:
            c = i[1] - i[0]
            diff.append((c , i[0] , i[1]))
        diff.sort()
        total = 0
        a = 0
        b = len(costs) - 1
        while a < b:
            total += diff[a][2] + diff[b][1]
            a += 1
            b -= 1
        return total   

        
        