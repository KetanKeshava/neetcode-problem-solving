class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visitedMap = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in visitedMap:
                return [visitedMap.get(complement), i]
            visitedMap[nums[i]] = i 


#visitedMap {}
