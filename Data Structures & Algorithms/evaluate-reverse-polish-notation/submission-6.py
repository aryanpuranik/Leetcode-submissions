class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        
        for i in tokens:
            if i == "+":
                sums =stack.pop() + stack.pop() 
                stack.append(sums)
            elif i == "*":
                mult = stack.pop() * stack.pop()
                stack.append(mult)
            elif i == "-":
                a = stack.pop()
                diff = stack.pop() - a
                stack.append(diff)
            elif i == "/":
                a = stack.pop()
                div = int(stack.pop() / a)
                stack.append(div)
            else:
                stack.append(int(i))
        return stack[-1]