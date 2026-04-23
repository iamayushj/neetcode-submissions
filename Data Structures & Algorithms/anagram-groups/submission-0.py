class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            keyOfMap = "".join(sorted(word))
            groups[keyOfMap].append(word)
        
        return list(groups.values())