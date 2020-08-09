class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 1
        r = num
        while l <= r:
            mid = (l + r) // 2
            print(l, r, mid)
            pow_mid = mid ** 2
            if pow_mid == num:
                return True
            if pow_mid < num:
                l = mid + 1
            if pow_mid > num:
                r = mid - 1
        return False
        
a = Solution()
# a.isPerfectSquare(16)
a.isPerfectSquare(104976)