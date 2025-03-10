class Solution:
    def plusOne(self, digits):
        for i in range(len(digits) - 1, - 1, - 1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            cur = digits[i] + carry
            digits[i] = cur % 10
            carry = cur // 10
        if carry:
            return [carry]+digits
        return digits