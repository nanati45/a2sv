class TimeMap:

    def __init__(self):
       self.store = defaultdict(list)
       self.times = defaultdict(str) 

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append(timestamp)
        self.times[timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if self.store[key]:
            idx = bisect_right(self.store[key] , timestamp)
            if idx == 0 :
                return "" 
            else:
                return self.times[self.store[key][idx - 1]]    
        else:
            return ""    



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)