class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closetopen = {")":"(","]":"[", "}":"{"}

        for i in s:
            if i in closetopen:
                if stack and stack[-1]==closetopen[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        if not stack:
            return True
        else:
            return False