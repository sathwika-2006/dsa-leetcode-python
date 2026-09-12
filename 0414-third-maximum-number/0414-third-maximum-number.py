class Solution(object):
    def thirdMax(self, nums):
        first=float('-inf')
        second=float('-inf')
        third=float('-inf')
        for i in range(len(nums)):
            if nums[i]==first or nums[i]==second or nums[i]==third:
                continue
            if nums[i]>first:
                third=second
                second=first
                first=nums[i]
            elif nums[i]>second:
                third=second
                second=nums[i]
            elif nums[i]>third:
                third=nums[i]
        if third==float('-inf'):
            return first
        else:
            return third

        