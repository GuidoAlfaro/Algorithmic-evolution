class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        L = 0
        for i in range(len(nums)):
            if (nums[i] != 0):
                nums[L], nums[i] = nums[i], nums[L]
                L += 1