class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def fact(num):
            if num < 2:
                return 1

            return num * fact(num - 1)   
        ls = []
        for i in range(rowIndex + 1):
            n = (fact(rowIndex)/ (fact(rowIndex - i) * fact(i)))
            ls.append(int(n))
        return ls    