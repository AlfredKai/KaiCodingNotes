class Solution(object):

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        r = 0
        negative = x < 0
        if x < 0:
            x = -x
        while x > 0:
            if r != 0:
                r *= 10
            r += (x % 10)
            x = (int)(x / 10)
        if r > 2147483647 or r < -2147483648:
            return 0
        return -r if negative else r
    

a = Solution()


print(a.reverse(123))
print(a.reverse(-123))
print(a.reverse(120))
print(a.reverse(0))
print(a.reverse(1534236469)) # expected: 0