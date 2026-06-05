class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left = right = 0
        while right < len(nums):
            while right < len(nums) and nums[right] % 2 != 0:
                right += 1
            if right < len(nums):
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right += 1
        return nums