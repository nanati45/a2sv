class Solution:
    def smallestNumber(self, num: int) -> int:
        if num > 0:
            num = sorted(str(num))
            if num[0] == "0":
                for i in range(1, len(num)):
                    if num[i] != "0":
                        num[0], num[i] = num[i], num[0]
                        break
            return int("".join(num))
        elif num < 0:
            num = sorted(str(-num), reverse=True)
            return -int("".join(num))
        else:
            return 0             

