class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        current = "1"

        for _ in range(2, n + 1):
            next_seq = []
            count = 1

            # Iterate through the current sequence and count consecutive digits
            for i in range(1, len(current)):
                if current[i] == current[i - 1]:
                    count += 1
                else:
                    next_seq.append(str(count))
                    next_seq.append(current[i - 1])
                    count = 1

            # Add the last group
            next_seq.append(str(count))
            next_seq.append(current[-1])

            # Update current sequence
            current = ''.join(next_seq)

        return current