class Solution:
    def countSeniors(self, details: List[str]) -> int:
        counter = 0
        for person in details:
            if int(person[11:13]) > 60:
                counter += 1
        return counter