class Solution:

    from math import gcd

    def gcdOfOddEvenSums(self, n: int) -> int:
        odd = []
        even = []

        i = 1
        while len(odd) < n and len(even) < n:
            if i % 2 != 0:
                odd.append(i)
                i += 1
            else:
                even.append(i)
                i += 1
        
        return gcd(sum(odd), sum(even))
