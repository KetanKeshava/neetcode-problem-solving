class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros, ones, twos = 0,0,0
        
        for num in nums:
            if num == 0:
                zeros += 1
            elif num == 1:
                ones += 1
            else: 
                twos +=1
        # print(zeros, ones, twos)

        write = 0

        while write < zeros:
            nums[write] = 0
            write +=1

        while write < (zeros + ones):
            nums[write] = 1
            write +=1

        while write < len(nums):
            nums[write] = 2
            write +=1

        # print(nums)
