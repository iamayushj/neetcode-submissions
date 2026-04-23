class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res_map={}
        #[1,1, 2,2,2,2 3,3,3]
        #store element value as key and their count as value in this map
        #res_map {(1,2) (2,4) (3, 3)}
        for x in nums:
            res_map[x] = res_map.get(x,0) + 1
        freq = [[] for y in range(len(nums) + 1)]

        for index, value in res_map.items():
           freq[value].append(index)
        
        result = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result