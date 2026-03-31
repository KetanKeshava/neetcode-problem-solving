class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freqMap = {}
        for num in nums:
            if num in freqMap:
                return True
            else:
                freqMap[num] = 1
        return False

        