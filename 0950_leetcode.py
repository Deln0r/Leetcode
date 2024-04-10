class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        q = []
        for ele in deck[::-1]:
            if not q:
                q.append(ele)
            else:
                q.insert(0,q.pop())
                q.insert(0,ele)
        print(q)
        return q