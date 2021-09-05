class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = 2*length*[0]
        for i in range(len(ans)):
            ans[i] = nums[i%length]
        return ans
