class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            if char in "+-*/":
                op2 = stack.pop()
                op1 = stack.pop()

                if char == "+":
                    res = op1 + op2
                elif char == "-":
                    res = op1 - op2
                elif char == "*":
                    res = op1 * op2
                else:
                    res = int(op1 / op2)

                stack.append(res)

            else:
                stack.append(int(char))

        return stack.pop()