class Solution:
    from math import gcd

    def gcdSum(self, nums: list[int]) -> int:
        
        n = len(nums)
        max_num = nums[0]
        m = [nums[0]]

        for num in nums[1:]:
            if num > max_num :
                max_num = num
            m.append(max_num)
        
        sorted_prefixGcd = sorted(gcd(nums[i], m[i]) for i in range(n))

        l, r = 0, n - 1

        ans = 0
        while l < r :
            ans += gcd(sorted_prefixGcd[l], sorted_prefixGcd[r])
            l += 1
            r -= 1

        return ans
