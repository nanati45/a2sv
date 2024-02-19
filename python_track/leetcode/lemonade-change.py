class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        l = 0
        while l< len(bills) :
            if bills[l] == 5:
                five += 1
            elif bills[l] == 10 :
                ten +=1
                if five == 0:
                    return False
                five -=1 
            else:
                if ten == 0 and five < 3:
                    return False
                elif ten and five:
                    ten  -=1 
                    five -=1
                elif five >= 3:
                    five -= 3
                else:
                    return False
            l += 1
        return True               

                               
        