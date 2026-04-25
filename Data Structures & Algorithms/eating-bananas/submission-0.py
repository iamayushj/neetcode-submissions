class Solution:
    def can_finish(self, k, piles, h):
        total_time = 0
        for i in piles:
            total_time += (i + k - 1) // k #ceil(i / k)
            if total_time > h:
                return False
        return total_time <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while (left <= right):
            mid = (left + right) // 2
            if (self.can_finish(mid, piles, h)):
                right = mid - 1
            else:
                left = mid + 1
        return left
