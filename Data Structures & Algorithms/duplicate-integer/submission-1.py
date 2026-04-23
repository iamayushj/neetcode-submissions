class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

#hashmap solution
        #my_map = {}
       # for x in nums:
       #     if x in my_map:
        #        return True
        #    my_map[x] = True
        #return False

#set solution
        return (len(set(nums)) < len(nums))