class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
#low 3 high 5 mid 4
        while (low < high):
            mid = (low + high)//2
            print("low", low)
            print("mid", mid)
            print("high", high)
            print("nums[mid]", nums[mid])
            print("nums[high]", nums[high]) 
            if (nums[mid] > nums[high]):
                low = mid + 1
                #print("low", low)
            else:
                high = mid
                #print("high", high)
        return nums[low]
