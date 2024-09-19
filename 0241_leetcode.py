class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def compute(left: List[int], right: List[int], op: str) -> List[int]:
            results = []
            for l in left:
                for r in right:
                    if op == '+':
                        results.append(l + r)
                    elif op == '-':
                        results.append(l - r)
                    elif op == '*':
                        results.append(l * r)
            return results

        if expression.isdigit():
            return [int(expression)]

        results = []
        for i, char in enumerate(expression):
            if char in '+-*':
                left_expr = expression[:i]
                right_expr = expression[i+1:]
                left_results = self.diffWaysToCompute(left_expr)
                right_results = self.diffWaysToCompute(right_expr)
                results.extend(compute(left_results, right_results, char))
        
        return results