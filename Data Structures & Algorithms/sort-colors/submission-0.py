class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # using bucket sort since we have a exhaustive range of values in this case - 3 (0-Red, 1-White, 2-Blue)
        counts = [0,0,0]

        for i, num in enumerate(nums):
            counts[num] += 1

        ans = 0
        for n in range(len(counts)):
            for j in range(counts[n]):
                nums[ans] = n
                ans += 1

        
        