class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            d[n]=i

        for i, n in enumerate(nums):
            pair = target - n
            if pair in d and i != d[pair]:
                return i, d[pair]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for i,n in enumerate(nums):
            if target-n in dict:
                return dict[target-n],i
            dict[n]=i