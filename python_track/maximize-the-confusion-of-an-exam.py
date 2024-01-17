class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        def maxConsec(change,k ):
            left = 0
            right = 0
            n = len(answerKey)
            mx = 0
            while right < n:
                if answerKey[right] == change:
                    k -=1
                while k < 0:
                    if answerKey[left] == change:
                        k +=1
                    left +=1 
                mx = max(mx, right - left+1)
                right +=1  

            return mx  
                

        return max(maxConsec("T",k) , maxConsec("F",k) )



        