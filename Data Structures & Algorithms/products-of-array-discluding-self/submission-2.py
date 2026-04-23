class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        prefix = 1
        suffix = 1
        for x in range(len(nums)):
            result[x] = result[x] * prefix
            prefix = prefix * nums[x]
            #print(prefix)

        #print(result)
        for y in range(len(nums)-1, -1, -1):
            result[y] = result[y] * suffix
            #print(result)
            suffix = suffix * nums[y]
            #print(suffix)

        return result
        '''total = 1
        result = []
        without_zero_total = 1
        for x in nums:
            total = x * total
        #print(total)

        if total == 0:
            for x in nums:
                if x == 0:
                    without_zero_total = without_zero_total * 1
                else:
                    without_zero_total = without_zero_total * x

        if nums.count(0) > 1:
            total = 0
            without_zero_total = 0

        for z in nums:
            #print(int(total/1))
            if total == 0 and z == 0:
                result.append(int(without_zero_total))
            else:
                result.append(int(total/z))
        
        return result
        '''