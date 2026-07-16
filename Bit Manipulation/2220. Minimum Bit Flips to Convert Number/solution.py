class Solution:

    def dectobin(self, num):
        result = []
        while num > 1:
            result.append(num % 2)
            num = num // 2
        result.append(num)

        return result[::-1]

    def minBitFlips(self, start: int, goal: int) -> int:
        
        a = self.dectobin(start)
        b = self.dectobin(goal)

        l = max(len(a), len(b))

        if len(a) < l:
            a = ([0] * (l-len(a))) + a
        elif len(b) < l:
            b = ([0] * (l-len(b))) + b

        count = 0

        for i in range(l-1,-1,-1):
            if a[i] != b[i]:
                count += 1
            
        return count
