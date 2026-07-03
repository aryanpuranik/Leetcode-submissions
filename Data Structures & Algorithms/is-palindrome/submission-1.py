class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        map1 = []
        map2 = []

        for i in s:
            if i.isalnum():
                map1.append(i)
        for i in s[::-1]:
            if i.isalnum():
                map2.append(i)
        print(map2)
        if map1==map2:
            return True
        return False