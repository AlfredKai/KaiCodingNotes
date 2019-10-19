from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        r = []
        for i in range(0, len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 1
            else:
                count[nums[i]] += 1

        countList = [(k, v) for k, v in count.items()]

        countList.sort(key = lambda x: x[1], reverse = True)

        for i in range(0, k):
            r.append(countList[i][0])

        return r

a = Solution()
print(a.topKFrequent([1,1,1,2,2,3], 2))

print(a.topKFrequent([1], 1))

