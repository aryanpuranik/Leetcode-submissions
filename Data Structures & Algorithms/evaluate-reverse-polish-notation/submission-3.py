class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for i in tokens:

            if i =="+":
                a = int(stack.pop())+int(stack.pop())
                stack.append(a)
            elif i == "-":
                a=int(stack.pop())
                b=int(stack.pop())
                stack.append(b-a)
            elif i == "*":
                a = int(stack.pop())*int(stack.pop())
                stack.append(a)
            elif i == "/":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(int(b/a))
            else:
                stack.append(int(i))
        
        return stack[-1]