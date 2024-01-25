class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.generated = {}
        self.timeToLive = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.generated[tokenId] = currentTime + self.timeToLive       

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.generated:
            if currentTime < self.generated[tokenId]:
                self.generated[tokenId] = currentTime + self.timeToLive
            

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for token, expiry_date in self.generated.items():
            if currentTime < expiry_date:
                count += 1
        
        return count



# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)