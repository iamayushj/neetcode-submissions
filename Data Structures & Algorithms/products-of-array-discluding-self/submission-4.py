class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      result = [1] * len(nums)
      left_product = 1
      right_product = 1
      #for k, v in enumerate(nums):
      for i in range(0,len(nums)):
        result[i] = result[i] * left_product
        left_product = left_product * nums[i]

      for j in range(len(nums) - 1, -1, -1):
        result[j] = result[j] * right_product
        right_product = right_product * nums[j]

      return result