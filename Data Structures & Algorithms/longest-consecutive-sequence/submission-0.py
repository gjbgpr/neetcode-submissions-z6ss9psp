class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set()
        for num in nums:
            hset.add(num)

        max_count = 0
        for num in hset:
            if num - 1 not in hset:
                count = 0
                current_num = num
                while current_num in hset:
                    count += 1
                    current_num += 1
                max_count = max(max_count, count)
        return max_count