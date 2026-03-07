class Solution:
    def isValid(self, s: str) -> bool:
        signs = {"]":"[", "}":"{",")":"("}
        stack = []
        for i in s:
            if i not in signs:
                stack.append(i)
            elif not stack or signs[i] != stack.pop():                
                return False
        return len(stack) == 0