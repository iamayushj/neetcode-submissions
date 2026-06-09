class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      set_nums = set(nums)
      max_length = 0
      for i in set_nums:
        if (i-1) not in set_nums:
          counter = 1
          while (counter + i) in set_nums:
            counter += 1
          max_length = max(max_length, counter)
      return max_length