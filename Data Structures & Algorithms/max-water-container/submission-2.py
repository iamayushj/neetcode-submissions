class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Water = (j - i) * min(height[i], height[j])
          maxAreaCalc = 0
          key = 0
         #for key in range(0, len(heights)):
          left  = key
          right = len(heights) - 1
          #[1,7,2,5,4,7,3,6]
          #left = 0
          #right = 7
          while (left < right):
            maxAreaCalc = max((right - left) * min(heights[left] , heights[right]), maxAreaCalc)
            #left+=1
            if heights[left] > heights[right]:
              right-= 1
            else:
              left+=1
          return maxAreaCalc