class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set()
        for num in nums:
            hset.add(num)
        
        result = 0
        for num in hset:
            if num - 1 not in hset:
                count = 1
                current = num
                while current + 1 in hset:
                    count += 1
                    current += 1
                result = max(result, count)
        return result