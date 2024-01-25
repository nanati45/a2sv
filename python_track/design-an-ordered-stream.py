class OrderedStream:

    def __init__(self, n: int):
        self.vals = [None] * n
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.vals[idKey- 1] = value
        if self.ptr == idKey-1:
            while self.ptr < len(self.vals) and self.vals[self.ptr] != None:
               self.ptr += 1

            return self.vals[idKey-1:self.ptr]
        return []    

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)