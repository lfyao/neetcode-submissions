class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        current_sum = numbers[l] + numbers[r]
        while current_sum != target:
            if current_sum < target:
                l += 1
            if current_sum > target:
                r -= 1
            current_sum = numbers[l] + numbers[r]
        
        return [l + 1, r + 1]
            