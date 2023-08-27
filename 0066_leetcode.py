class Solution:
    def plusOne(self, digits):
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            carry, digits[i] = divmod(digits[i] + carry, 10)
        return digits if not carry else [carry] + digits
