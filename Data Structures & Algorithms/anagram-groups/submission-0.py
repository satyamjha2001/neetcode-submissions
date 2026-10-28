class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for item in strs:
            key = ''.join(sorted(item))
            if key not in groups:
                groups[key] = [item]
            else:
                groups[key].append(item)
        return list(groups.values())