class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prod = 1
        # no_of_zeros = 0
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         no_of_zeros += 1
        #     else:
        #         prod = nums[i] * prod

        # for i in range(len(nums)):
        #     if no_of_zeros == 0:
        #         nums[i] = prod // nums[i]
        #     elif no_of_zeros > 1:
        #         nums[i] = 0
        #     else:
        #         if nums[i] == 0:
        #             nums[i] = prod
        #         else: 
        #             nums[i] = 0
        # return nums

        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) -1, -1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        return res