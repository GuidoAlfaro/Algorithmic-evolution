class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)
        r_nums = [[] for i in range(len(nums) + 1)]
        for n, c in freq.items():
            r_nums[c].append(n)
        res = []
        for lists in reversed(r_nums):
            for i in lists:
                res.append(i)
                if(len(res) == k):
                    return res