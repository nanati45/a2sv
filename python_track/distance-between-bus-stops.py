class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
            if destination>start:
                s=sum(distance[start:destination])
            elif start>destination:
                s=sum(distance[destination:start])
            else:
                s=0 
            total=sum(distance)
            anti=total-s
            return min(s,anti)       
