import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        pile_max_bananas = max(piles)

        l = 1
        r = max(piles)

        ans = max(piles) #atleast this is one of the possible speeds

        while l <= r:
            k = (l + r) // 2
            
            hours = 0
            for i in range(len(piles)):
                hours += math.ceil(piles[i] / k)
            
            if hours <= h:
                ans = min(ans, k)
                r = k - 1
            elif hours > h:
                l = k + 1

        return ans

            

        

        


        