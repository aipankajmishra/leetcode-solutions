class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = x
        return str(x) == (str(y)[-1::-1])
