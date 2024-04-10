class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = (tickets[k] - 1) * len(tickets) + k + 1
        for i in range(k):
            if tickets[i] < tickets[k]:
                count -= tickets[k] - tickets[i]
        
        for i in range(k + 1, len(tickets)):
            if tickets[i] < tickets[k] - 1:
                count -= tickets[k] - 1 - tickets[i]
        
        return count