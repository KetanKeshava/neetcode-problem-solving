class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        VisitedEle = {}
        for i , num in enumerate(nums):
            compliment = target - num
            if compliment in VisitedEle:
                return [VisitedEle[compliment], i]
            VisitedEle[num] = i
