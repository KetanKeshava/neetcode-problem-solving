class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map_set = set()
        for n in nums:
            if n in map_set :
                return True
            map_set.add(n)
        return False
        