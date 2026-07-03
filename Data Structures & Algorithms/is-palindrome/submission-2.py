class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Clean the string
        s = ''.join(c.lower() for c in s if c.isalnum())
        print(s)
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False

        return True