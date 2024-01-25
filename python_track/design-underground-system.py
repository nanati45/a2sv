class UndergroundSystem:

    def __init__(self):
        self.In = {}
        self.out = defaultdict(list)
    
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.In[id] = [stationName , t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation , sTime = self.In[id]
        if id in self.In and t > sTime:
            self.out[(startStation , stationName)].append(t - sTime) 
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if (startStation , endStation) in self.out:
            total = sum(self.out[(startStation , endStation)])
            leng = len(self.out[(startStation , endStation)])
            return total / leng
        return float(0)

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)