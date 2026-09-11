class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        expected_sum=n*(n+1)//2
        actual_sum=0
        for i in range(0,n):
            actual_sum=actual_sum+nums[i]
        missing=expected_sum-actual_sum
        return missing