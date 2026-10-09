from math import ceil

class Solution:
    def canEatWithSpeed(self, piles, h, k):
        hours = 0
        for bananas in piles:
            hours += ceil(bananas / k)

        if hours <= h:
            # return YES
            return True

        else:
            # return NO
            return False

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        ans = high

        while low <= high:
            mid = (low + high) // 2

            if self.canEatWithSpeed(piles, h, mid):
                # This may be the first FLIP
                ans = mid
                
                # or the first FLIP might be a lower speed
                high = mid - 1

            else:
                # the first FLIP is definitely greater than spped mid
                low = mid + 1

        return ans

    


        