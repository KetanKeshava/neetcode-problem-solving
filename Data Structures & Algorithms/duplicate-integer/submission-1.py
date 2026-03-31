class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for r in range(1,len(nums)):
            if nums[r] == nums[r-1]:
                return True
        return False
        