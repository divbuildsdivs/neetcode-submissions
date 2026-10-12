class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        N = len(s)
        freq = [0 for i in range(26)]
        l = 0
        r = 0
        maxWindow = 0
        maxFreq = 0
        while r < N:
            currWindow = r - l + 1
            ch = s[r]
            index = ord(ch) - ord('A')
            freq[index] += 1
            maxFreq = max(maxFreq, freq[index])
            if currWindow > maxFreq + k:
                
                freq[ ord(s[l]) - ord('A')] -= 1
                l += 1

                #Not changing maxFreq as it will not make any diff
                #as long as the current maxFreq doesnot increases,
                #this condition will still be true 
                #to make currWindow = maxFreq + k, freq of a char has to anyway surpass this maxFreq as this maxFreq for current window length is not enough
            else:
                maxWindow = max(maxWindow, currWindow)
            
            r += 1

        return maxWindow