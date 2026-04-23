class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #nums = [-2, 0, 1, 1, 2]
        new_nums = sorted(nums)
        result = []
        #print(new_nums)

        for x, y in enumerate(new_nums):
            j = x + 1
            k = len(nums) - 1
            if x > 0 and new_nums[x-1] == new_nums[x]:
                continue
            while j < k:
              target = -new_nums[x]
              #print("target is" , target)
              if target == (new_nums[j] + new_nums[k]):
                result.append([new_nums[x], new_nums[j], new_nums[k]])
                j+=1
                k-=1

                while j < k and new_nums[j] == new_nums[j - 1]:
                  j +=1
                while j < k and new_nums[k] == new_nums[k + 1]:
                  k -= 1                  
              elif target > (new_nums[j] + new_nums[k]):
                j+=1
              elif target < (new_nums[j] + new_nums[k]):
                k-=1
        return result
