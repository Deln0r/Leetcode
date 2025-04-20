
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        # Assumption: the same number means same color in a greedy manner. 
        # Also, the number of rabbits in a group = answers[i] + 1
        count = Counter(answers)
        min_rabbits = 0
        
        for answer, freq in count.items():
            group_size = answer + 1
            num_groups = ceil(freq / group_size)
            min_rabbits += num_groups * group_size
        
        return min_rabbits