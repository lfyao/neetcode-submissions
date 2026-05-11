class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for string in strs:
            res += f'{len(string)}#{string}'
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        j = 1

        while i < len(s):
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        
        return res