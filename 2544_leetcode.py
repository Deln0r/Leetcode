# class Solution:
#     def alternateDigitSum(self, n: int) -> int:
#         result=str(n)
#         sum=0
#         for i in range(len(result)):
#             if i%2 ==0:
#                 sum=sum+int(result[i])
#             else:  
#                 sum=sum-int(result[i])  
#         return sum 

def alternateDigitSum(n):
    arr = []
    while n:
        arr.append(n % 10)
        n = n // 10
    arr.reverse()
    for i in range(len(arr)):
        if i % 2 != 0:
            arr[i] = -arr[i]
    return sum(arr)


n = 886996

print(alternateDigitSum(n))