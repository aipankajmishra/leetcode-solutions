class Solution:
    def mySqrt(self, x: int) -> int:
        lower,upper = 0, x
        while lower <= upper:
            sq = (upper+lower)//2
            if (sq*sq < x):
                lower = sq+1
            elif (sq*sq > x):
                upper = sq - 1
            else:
                return sq
        return upper
