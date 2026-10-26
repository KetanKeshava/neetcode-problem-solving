class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        if len(nums) == 0:
            return [[],]

        result = []
        
        for num in nums:
            if len(result) == 0:
                # first element
                result.extend([[], [nums[0]]])
            else:
                result_to_include_num = []
                for subarray in result:
                    new_arr = list(subarray)
                    new_arr.append(num)
                    result_to_include_num.append(new_arr)

                result.extend(result_to_include_num)

        print(result)

        return result
                



        

        