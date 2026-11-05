class Solution:    
    def get_time(self, l: List[int], r: int) -> int:
        t = 0
        for num in l:
            t += (num + r - 1) // r
        return t

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l <= r:
            m = l + (r-l)//2
            time = self.get_time(piles, m)
            if time > h:
                l = m + 1
            else:
                r = m - 1
        return l
