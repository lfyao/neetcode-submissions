class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_products = [1]
        suffix_products = [1]
        prefix_holder = 1
        suffix_holder = 1
        i = 0
        while i < len(nums) -1 :
            prefix_holder *= nums[i]
            suffix_holder *= nums[len(nums) - i - 1]
            prefix_products.append(prefix_holder)
            suffix_products.append(suffix_holder)
            i += 1
        
        print(prefix_products, suffix_products)

        res = []
        j = 0
        while j < len(nums):
            res.append(prefix_products[j] * suffix_products[len(nums) - 1 - j])
            j += 1
        return res