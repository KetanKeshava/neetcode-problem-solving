class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = []
        subset = []

        def dfs(start, total):
            # base case
            if total == target:
                # save if subset does not exist and backtrack
                result.append(subset.copy())
                return
            
            if total > target:
                # prune branch
                return

            # n decisions
            for i in range(start, len(nums)):
                subset.append(nums[i])
                dfs(i, total + nums[i])

                subset.pop()

        dfs(0, 0)
        return result
                

        