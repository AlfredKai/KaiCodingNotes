from typing import List

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0] * len(nums2) for i in range(len(nums1))]

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if i == 0 and j == 0:
                    dp[i][j] = nums1[i] * nums2[j]
                    continue
                if i == 0:
                    dp[i][j] = max(dp[i][j-1], nums1[i] * nums2[j])
                    continue
                if j == 0:
                    dp[i][j] = max(dp[i-1][j], nums1[i] * nums2[j])
                    continue
                temp = nums1[i]*nums2[j] if dp[i-1][j-1] < 0 else dp[i-1][j-1] + nums1[i]*nums2[j]
                dp[i][j] = max(temp, max(dp[i-1][j], dp[i][j-1]))
        return dp[-1][-1]
