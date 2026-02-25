class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        word = {}
        word2 = {}
        for i in range(len(s)):
            word[s[i]] = 1 + word.get(s[i], 0)
            word2[t[i]] = 1 + word2.get(t[i], 0)
        return word == word2
            
        
