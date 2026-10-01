class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for token in tokens:
            
            try:
                # Try converting to int (handles negative numbers)
                stack.append(int(token))
            except ValueError:
                b = stack.pop()
                a = stack.pop()

                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    # Truncate toward zero
                    stack.append(int(a / b))
            print(token)
            print(stack)
        print(stack)
        return stack.pop()