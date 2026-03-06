class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        prefix = ""
        for i, s in enumerate(strs[0]):
            if(s == strs[-1][i]):
                prefix += s
            else:
                break
        return prefix