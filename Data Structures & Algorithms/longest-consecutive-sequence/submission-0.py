class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        r = 0
        store = set(nums)
        for n in nums:
            streak, curr = 0,n
            while curr in store:
                streak+=1
                curr +=1
            r = max(r, streak)
        return r
