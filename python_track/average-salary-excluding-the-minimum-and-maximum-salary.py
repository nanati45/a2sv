class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        min_=min(salary)
        max_=max(salary)
        for i in salary:
            if i==min_ or i==max_:
                salary.remove(i)
        print(salary)        
        return sum(salary)/len(salary)