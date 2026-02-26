class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prodIzq = 1
        prodDer = 1
        answer = [1] * len(nums)
        for i in range(len(nums)):
            answer[i] = prodIzq
            prodIzq *= nums[i]
        for k in reversed(range(len(nums))):
            answer[k] *= prodDer
            prodDer *= nums[k]
        return answer

