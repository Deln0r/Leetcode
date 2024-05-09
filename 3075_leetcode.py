class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        selected=0
        sum_happiness_value=0
        for happiness_value in happiness:
            if selected==k:
                return sum_happiness_value
            sum_happiness_value+=max(0,happiness_value-selected)
            selected+=1
      
        return  sum_happiness_value
