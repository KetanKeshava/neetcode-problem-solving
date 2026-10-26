class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []
        subset = []

        def dfs(i):
            if i == len(nums):
                # save subset and backtrack
                result.append(subset.copy())
                return

            # choice: include nums[i]
            subset.append(nums[i])
            dfs(i + 1)


            # choice: do not include nums[i]
            ## undo the addition of nums[i]
            subset.pop()
            dfs(i + 1)
            

        dfs(0)
        return result

                



        

        