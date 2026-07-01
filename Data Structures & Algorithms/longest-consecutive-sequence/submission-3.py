class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        r = 0
        store = set(nums)
        for n in nums:
            if n-1 not in store:
                streak, curr = 0,n
                while curr in store:
                    streak+=1
                    curr +=1
                r = max(r, streak)
        return r