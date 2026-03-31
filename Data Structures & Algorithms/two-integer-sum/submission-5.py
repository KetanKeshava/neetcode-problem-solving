class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapInt = {}
        for i, n in enumerate(nums) :
            if (target - n) in mapInt:
                return [mapInt[target-n], i]
            else:
                mapInt[n] = i
