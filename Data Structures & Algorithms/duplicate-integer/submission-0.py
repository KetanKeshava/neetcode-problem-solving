class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_num = {}
        for i in range(len(nums)):
            count_num[nums[i]] = 1 + count_num.get(nums[i], 0)
            if count_num[nums[i]] > 1:
                return True
        return False


        