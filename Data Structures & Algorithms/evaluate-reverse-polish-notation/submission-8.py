class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for op in tokens:
            if op.lstrip('-').isnumeric():
                stack.append(int(op))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                match op:
                    case '+':
                        stack.append(num2 + num1)
                    case '-':
                        stack.append(num2 - num1)
                    case '*':
                        stack.append(num2 * num1)
                    case '/':
                        stack.append(int(num2 / num1))
        return stack.pop()
                