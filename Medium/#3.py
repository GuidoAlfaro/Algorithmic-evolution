class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        indexs = {}
        longest = 0
        inicio = 0
        for i, w in enumerate(s):
            if(w in indexs):
                if(inicio <= indexs[w]):
                    inicio = indexs[w] + 1
            longest = max(i - inicio + 1, longest)
            indexs[w] = i
        return longest