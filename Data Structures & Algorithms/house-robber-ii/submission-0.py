class Solution:
    def _rob_linear(self, nums) -> int:
        if len(nums) < 3:
            return max(nums)

        prev_two = nums[0]
        prev_one = max(nums[0],nums[1])

        for i in range(2, len(nums)):
            curr = max(prev_two + nums[i], prev_one)
            prev_two = prev_one
            prev_one = curr
        
        return prev_one

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return max(nums)
        
        a1 = self._rob_linear(nums[:n-1])
        a2 = self._rob_linear(nums[1:])
        return max(a1,a2)
        