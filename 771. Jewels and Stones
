class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count,counter = 0,Counter(stones)
        for x in jewels:
            count = count + counter[x]
        return count
