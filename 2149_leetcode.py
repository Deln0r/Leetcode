class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives = list(filter(lambda x: x > 0, nums))
        negatives = list(filter(lambda x: x < 0, nums))

        res = []
        for i in range(len(nums)//2):
            res.append(positives[i])
            res.append(negatives[i])
        
        return res