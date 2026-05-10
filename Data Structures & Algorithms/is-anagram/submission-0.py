class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_letter_count = {}
        t_letter_count = {}
        
        for char in s:
            s_letter_count[char] = s_letter_count.get(char, 0) + 1
            
        for char in t:
            t_letter_count[char] = t_letter_count.get(char, 0) + 1

        similarity_check = None
        for key in s_letter_count:
            if (not key in t_letter_count) or (s_letter_count[key] != t_letter_count[key]):
                return False
            similarity_check = True
        return similarity_check