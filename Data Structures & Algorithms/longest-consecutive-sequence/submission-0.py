class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        counter = 1
        set_input = set(nums)
        max_length = 0
        for i in set_input:
            if (i-1) not in set_input:
              #result_set = set()
              #result_set.add(i)
              counter = 1
              while (i + counter) in set_input:
                #result_set.add(i + counter)
                #print(result_set)
                counter+= 1
                #if max_length < counter: #< len(result_set):
                    #max_length = len(result_set)
              max_length = max(max_length, counter)
            else:
                counter = 0
        return max_length