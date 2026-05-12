class Solution:
    def isPalindrome(self, s: str) -> bool:
        head_pointer = 0
        tail_pointer = len(s) - 1

        while head_pointer < tail_pointer:
            while head_pointer < tail_pointer and not s[head_pointer].isalnum():
                head_pointer += 1
            while head_pointer < tail_pointer and not s[tail_pointer].isalnum():
                tail_pointer -= 1
            if s[head_pointer].lower() != s[tail_pointer].lower():
                return False
            head_pointer += 1
            tail_pointer -= 1

        return True