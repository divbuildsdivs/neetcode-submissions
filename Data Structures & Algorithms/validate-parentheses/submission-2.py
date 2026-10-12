class Solution:
    def isValid(self, s: str) -> bool:
        N = len(s)
        stack = []
        for i in range(N):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                stack.append(s[i])
            elif (len(stack) == 0):
                return False
            elif (s[i] == "}" and stack.pop(-1) == "{") or (s[i] == "]" and stack.pop(-1) == "[") or (s[i] == ")" and stack.pop(-1) == "("):
                continue
            else:
                return False
        return len(stack) == 0
        