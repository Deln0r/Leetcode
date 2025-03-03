class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left,right = [],[]
        for ele in nums:
            if ele<pivot:
                left.append(ele)
            elif ele>pivot:
                right.append(ele)
        return left+[pivot]*(len(nums)-len(left)-len(right))+right