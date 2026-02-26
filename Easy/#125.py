class Solution:
    def isPalindrome(self, s: str) -> bool:
        resultado = "".join(c.lower() for c in s if c.isalnum())
        return resultado == resultado[::-1]
