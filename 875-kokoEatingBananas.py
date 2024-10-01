class Solution:
    # Time: O(nlogm), n = len(piles), m = max(piles)
    # Space: O(1)

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # this is the most important line, if you can't come up with this line, you can't solve this problem
        # we are using binary search on the max(piles) array from 1 to max(piles)
        # why? because the max speed to eat the bananas is the max(piles)
        # so the answer should be in the range of 1 to max(piles)
        l, r = 1, max(piles)
        res = r

        while l <= r: # log(m) steps here
            k = (l + r) // 2

            # these lines(10-13) calculate the total time needed to eat all the bananas
            totalTime = 0
            for p in piles: # n steps here
                # we round up to the nearest int use math.ceil
                totalTime += math.ceil(p / k)
            
            if totalTime <= h:
                # since we are checking the smaller half, so we don't need to use min func here
                res = k
                r = k - 1
            else:
                l = k + 1
        
        return res