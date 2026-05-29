class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res_map = {}

        for index, value in enumerate(nums):
            res_map[value] = index
        
        for index, value in enumerate(nums):
            difference = target - value
            if difference in res_map and res_map[difference] != index:
                return[index, res_map[difference]]
        
        return []
