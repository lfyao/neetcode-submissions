class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return 'thelistwasemptyreturnanemptylist'
        return 'thisismydelimiterstring'.join(strs)

    def decode(self, s: str) -> List[str]:
        if (s == 'thelistwasemptyreturnanemptylist'):
            return []
        return s.split('thisismydelimiterstring')