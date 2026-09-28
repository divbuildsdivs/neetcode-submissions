class Solution:
    def isPalindrome(self, s: str) -> bool:
        N = len(s)
        l = 0
        r = N-1
        lowerText = s.lower()
        while l <= r:
            
            if not lowerText[l].isalnum():
                l +=1
                continue
            if not lowerText[r].isalnum():
                r -= 1
                continue
            if lowerText[l] != lowerText[r]:
                return False
            l += 1
            r -= 1
        return True
        