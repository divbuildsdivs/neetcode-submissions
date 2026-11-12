class Solution:
    def validPalindrome(self, s: str) -> bool:
        N = len(s)
        def isPallindrome(l, r, e):
            nonlocal s
            while l < r:
                if s[l] != s[r]:
                    if e == 0:
                        return isPallindrome(l + 1, r, e+1) or isPallindrome(l, r - 1, e+1)
                    else:
                        return False
                l += 1
                r -= 1
                print(e)
            return True
        return isPallindrome(0, N-1, 0)
