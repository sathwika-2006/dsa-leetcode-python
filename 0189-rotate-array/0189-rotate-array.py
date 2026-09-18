class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        last_part = nums[-k:]
        first_part = nums[:-k]
        nums[:] = last_part + first_part