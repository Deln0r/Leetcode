class Solution:
    def countLargestGroup(self, n: int) -> int:
        # Solution 1: 
        digit_sums = [0] * (n + 1)
        for num in range(1, n + 1):
            digit_sums[num] = digit_sums[num // 10] + (num % 10)

        group_counts = Counter(digit_sums[1:])  
        largest_group_size = max(group_counts.values())
        return sum(1 for count in group_counts.values() 
                   if count == largest_group_size)