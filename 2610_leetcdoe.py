class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        list_of_sets = [set()]
        def find_set(n):
            for sety in list_of_sets:
                if num not in sety:
                    sety.add(num)
                    return
            empty_set = set()
            empty_set.add(num)
            list_of_sets.append(empty_set) 
             
                    
        for num in nums:
            find_set(num)
        return [list(sety) for sety in list_of_sets]
