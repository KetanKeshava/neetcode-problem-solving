class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqS = {}
        freqT = {}

        if len(s) != len(t):
            return False
        for i in range(len(s)):
            freqS[s[i]] = freqS.get(s[i], 0) + 1
            freqT[t[i]] = freqT.get(t[i], 0) + 1

        for char in freqS.keys():
            if freqS.get(char,0) != freqT.get(char,0):
                return False
        return True

        

        