class Solution:
    def evalRPN(self, tokens):
        import math
        opt = set(["+", "-", "*", "/"])
        stack = []
        for n in tokens:
            if len(stack) >= 2 and n in opt:
                if n == "+":
                    stack.append(stack.pop(-1) + stack.pop(-1))
                if n == "-":
                    temp = stack.pop(-1)
                    stack.append(stack.pop(-1) - temp)
                if n == "*":
                    stack.append(stack.pop(-1) * stack.pop(-1))
                if n == "/":
                    temp = stack.pop(-1)
                    stack.append(math.trunc(stack.pop(-1) / temp))
            else:
                stack.append(int(n))

        return stack.pop(-1)

x = Solution()
print(x.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))