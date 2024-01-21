class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # using an array to store the number of passengers at the starting and ending points of the trips

        passengers = [0] * 1001
        for trip in trips :
            numPass , start , end = trip 
            passengers[start] += numPass
            passengers[end] -= numPass

        
        currPass = 0
        for i in range(1001) :
            currPass += passengers[i]
            if capacity < currPass:
                return False
        return True
