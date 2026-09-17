class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleared = "".join(char.lower() for char in s if char.isalnum())
        reversed = cleared[::-1]

        if cleared == reversed:
            return True
        return False