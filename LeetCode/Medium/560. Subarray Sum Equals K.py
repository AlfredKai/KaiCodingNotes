from typing import List

# public class Solution {
#     public int subarraySum(int[] nums, int k) {
#         int count = 0, sum = 0;
#         HashMap < Integer, Integer > map = new HashMap < > ();
#         map.put(0, 1);
#         for (int i = 0; i < nums.length; i++) {
#             sum += nums[i];
#             if (map.containsKey(sum - k))
#                 count += map.get(sum - k);
#             map.put(sum, map.getOrDefault(sum, 0) + 1);
#         }
#         return count;
#     }
# }

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum = 0
        count = 0
        dic = {}
        dic[0] = 1
        for i in range(len(nums)):
            sum += nums[i]
            if sum - k in dic:
                count += dic.get(sum-k)
            dic[sum] = dic.get(sum,0) + 1
        return count

a = Solution()
# print(a.subarraySum([1,1,1],2))
print(a.subarraySum([1],1))