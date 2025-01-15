class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        num_set_bit1 = num1.bit_count()
        num_set_bit2 = num2.bit_count()

        if num_set_bit1 == num_set_bit2:
            return num1
        elif num_set_bit1 < num_set_bit2:
            # set k least significant bits of num1
            k = num_set_bit2 - num_set_bit1
            mask = 1
            while k:
                if num1 & mask == 0:
                    num1 |= mask
                    k -= 1
                mask <<= 1
            return num1
        else:
            # unset k least significant bits of num1
            k = num_set_bit1 - num_set_bit2
            mask = 1
            while k:
                if num1 & mask != 0:
                    # turn this off
                    num1 &= ~mask
                    k -= 1
                mask <<= 1
            return num1