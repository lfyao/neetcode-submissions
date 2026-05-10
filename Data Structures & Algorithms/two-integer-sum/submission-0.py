class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}

        for i, num in enumerate(nums):
            difference = target - num
            if difference in index_map:
                return [index_map[difference], i]
            index_map[num] = i