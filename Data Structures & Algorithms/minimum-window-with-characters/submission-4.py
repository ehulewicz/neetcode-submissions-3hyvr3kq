class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        if len(t) == 1:
            if s.find(t) == -1:
                return ""
            return t

        target_chars = set()
        target_counts = defaultdict(int)
        for c in t:
            target_chars.add(c)
            target_counts[c] += 1

        i, j = 0, 0
        current_counts = defaultdict(int)
        find = target_chars.copy()
        while j < len(s) and find:
            c = s[j]
            if c in target_chars:
                current_counts[c] += 1
                if current_counts[c] == target_counts[c]:
                    find.remove(c)
            j += 1
        if find:
            return ""

        j -= 1

        # keep track of what needs to be found as window slides right
        find = set()
        min_substring = (i, j)

        while True:
            if find:
                j += 1
                if j == len(s):
                    break

                c = s[j]
                if c in target_chars:
                    current_counts[c] += 1
                if c in find and current_counts[c] == target_counts[c]:
                    find.remove(c)
            else:
                min_substring = min(min_substring, (i, j), key=lambda x: x[1] - x[0])

                c = s[i]
                if c in target_chars:
                    current_counts[c] -= 1
                if current_counts[c] < target_counts[c]:
                    find.add(c)
                i += 1

        i, j = min_substring
        return s[i:j + 1]