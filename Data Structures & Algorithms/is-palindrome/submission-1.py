class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = []
        for i in s:
            if i.isalnum():
                s1.append(i.lower())
        return "".join(s1) == "".join(s1[::-1])