class Solution:
    def romanToInt(self, s: str) -> int:
        romanValues = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0

        for i in range(len(s) - 1, -1, -1):
            currValue = romanValues[s[i]]

            if i < len(s) - 1 and currValue < romanValues[s[i + 1]]:
                result -= currValue
            else:
                result += currValue

        return result