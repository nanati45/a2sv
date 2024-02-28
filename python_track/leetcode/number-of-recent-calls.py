class RecentCounter:

    def __init__(self):
        self.recents = deque()

    def ping(self, t: int) -> int:
        s = t - 3000
        self.recents.append(t)
        while self.recents and self.recents[0] < s :
            self.recents.popleft()
        return len(self.recents)    



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)