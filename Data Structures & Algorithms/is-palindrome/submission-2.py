class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleared = "".join(char.lower() for char in s if char.isalnum())
        for i in range(int((len(cleared))//2)):
            j = len(cleared) - i - 1
            if cleared[i] != cleared[j]:
                return False
        
        return True