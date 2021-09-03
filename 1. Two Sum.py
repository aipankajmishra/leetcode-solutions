class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        location = defaultdict(int)
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in location:
                return [i,location[diff]]
            location[nums[i]] = i
