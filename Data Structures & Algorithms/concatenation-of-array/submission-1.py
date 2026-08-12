class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        '''return (nums + nums)'''
        result = [0] * (2 * len(nums))
        for i in range(len(nums)):
            result[i] = nums[i]
            result[i + len(nums)] = nums[i]
        return result