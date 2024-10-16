class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        char_count = {"a": a, "b": b, "c": c}
        result = ""

        while char_count:
            sorted_chars = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
            max_char, max_count = sorted_chars[0]

            if len(result) >= 2 and result[-1] == result[-2] == max_char:
                if len(sorted_chars) > 1 and sorted_chars[1][1] > 0:
                    max_char = sorted_chars[1][0]
                else:
                    break

            if max_count <= 0:
                break

            result += max_char
            char_count[max_char] -= 1

        return result