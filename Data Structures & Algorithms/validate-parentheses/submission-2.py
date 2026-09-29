class Solution:
    def isValid(self, s: str) -> bool:
        dictt = {")":"(", "]": "[", "}":"{" }
        stack = []

        for i in range(len(s)):
            if s[i] in dictt:
                if stack and stack[-1] == dictt[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        if stack:
            return False
        else:
            return True