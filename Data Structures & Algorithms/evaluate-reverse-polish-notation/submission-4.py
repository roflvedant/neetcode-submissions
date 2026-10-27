class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        

        for r in tokens:

            if r == "+":
                n1 = (stack.pop())
                n2 = (stack.pop())
                stack.append(n1 + n2)
            elif r == "*":
                n1 = (stack.pop())
                n2 = (stack.pop())
                stack.append(n1 * n2)
            elif r == "-":
                n1 = stack.pop()
                n2 = (stack.pop())
                stack.append(n2 - n1)
            elif r == "/":
                n1 = (stack.pop())
                n2 = (stack.pop())
                stack.append(int(n2/n1))
            else:
                stack.append(int(r))
        
        return stack[0]