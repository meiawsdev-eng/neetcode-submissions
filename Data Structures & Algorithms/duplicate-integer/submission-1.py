class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        left = 0
        nums = sorted(nums)
        for i in range(1,len(nums)):
            if nums[left] == nums[i]:
                return True
            else:
                left += 1
        return False