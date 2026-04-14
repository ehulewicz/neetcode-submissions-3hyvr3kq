class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        groups = {}

        for s in strs:
            seen = [0] * 26
            a = ord('a')
            for c in s:
                seen[ord(c) - a] += 1

            seen = tuple(seen)
            if seen in groups:
                groups[seen].append(s)
            else:
                groups[seen] = [s]

        groups = [v for v in groups.values()]
        return groups