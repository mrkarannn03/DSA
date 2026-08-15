class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count = 0
        freq = {}
        l,r = 0,0
        for i in s:
            fc = freq.get(i, 0)
            if fc < 2:
                freq[i] = freq.get(i, 0) + 1
                r += 1
                count = max(count, r - l)
            else:
                while s[l] != i:
                    freq[s[l]] -= 1
                    l += 1
                freq[s[l]] -= 1
                l += 1
                freq[s[r]] += 1
                r += 1
                count = max(count, r - l)
        return count
