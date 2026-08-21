class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        check = defaultdict(int)
        for c in s1:
            check[c] += 1

        # window
        window = defaultdict(int)
        for i in range(len(s2)):
            window[s2[i]] += 1
            if i < len(s1):
                if window == check:
                    return True
                continue
            
            left_char = s2[i - len(s1)]
            window[left_char] -= 1

            if window[left_char] == 0:
                del window[left_char]

            if window == check:
                return True
        return False