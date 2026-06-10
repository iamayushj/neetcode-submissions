class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
      nums = sorted(nums)
      result = []
      #[-4, -1,-1, 0,1,2]
      #[-2, -1, 1, 2]
      for x, y in enumerate(nums):
        left  = x
        right = len(nums)-1
        mid = left + 1 

        if left > 0 and nums[left - 1] == nums[left]:
          continue
        while mid < right:
          if (nums[right] + nums[mid]) == -nums[left]:
            result.append([nums[left], nums[mid], nums[right]])
            mid += 1
            right -=1

            while (mid < right) and nums[mid] == nums[mid - 1]:
              mid += 1

            while (mid < right) and nums[right] == nums[right + 1]:
              right -= 1

          elif ( nums[right] + nums[mid]) > -nums[left]:
            right -= 1
          elif (nums[right] + nums[mid]) < -nums[left]:
            mid += 1
        
      return result