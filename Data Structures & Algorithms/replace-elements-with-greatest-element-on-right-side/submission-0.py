class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [0] * len(arr)
        maxRight = -1
        for i in range(len(arr)-1, -1, -1):
            ans[i] = maxRight
            maxRight = max(arr[i], maxRight)
        return ans
