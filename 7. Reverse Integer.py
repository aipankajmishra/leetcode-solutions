class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if x[0] == '-':
            y = x[-1:0:-1]
            val = int("-"+y)
            
        else:
            val = int(x[-1::-1])
        if (val < pow(-2,31) or val > pow(2,31)-1):
                return 0
        return val
