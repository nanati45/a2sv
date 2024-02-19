class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        minimum = points[0][1]
        arrows = 0
        for index in range(1,len(points)):
            if points[index][0] <= minimum:
                minimum = min(minimum,points[index][1])
                continue
            else:
                arrows += 1
                minimum = points[index][1]
        return arrows+1