class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i = 0
        len_ = len(arr)
        up = False
        down = False

        while i+1 < len_ and arr[i] < arr[i+1]:
            i += 1
            up = True
        
        while i+1 < len_ and arr[i] > arr[i+1]:
            i += 1
            down = True
        
        return i == len_ - 1 and up and down
    
    
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i = 0
        len_ = len(arr)

        while i+1 < len_ and arr[i] < arr[i+1]:
            i += 1
        
        if i == 0 or i == len_ -1:
            return False

        while i+1 < len_ and arr[i] > arr[i+1]:
            i += 1
        
        return i == len_ - 1