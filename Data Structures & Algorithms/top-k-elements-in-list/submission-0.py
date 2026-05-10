class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = {}
        count_num_map = {}
        for num in nums:
            old_count = num_freq.get(num)
            if old_count:
                count_num_map[old_count].remove(num)
            
            new_count = old_count + 1 if old_count else 1
            num_freq[num] = new_count
            
            if new_count in count_num_map:
                count_num_map[new_count].add(num)
            else: 
                count_num_map[new_count] = {num}
        
        res = []
        while len(res) < k:
            for key in reversed(count_num_map):
                for num in count_num_map[key]:
                    res.append(num)
                    if len(res) == k:
                        return res
                if len(res) == k:
                    return res
            
        return res