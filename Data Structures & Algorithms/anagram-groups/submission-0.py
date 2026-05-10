class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_patterns = {}
        
        for word in strs:
            letter_count = {
                'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0,
            }
            for letter in word:
                letter_count[letter] = letter_count.get(letter, 0) + 1

            anagram_key = tuple(letter_count.values())
            if anagram_key in anagram_patterns:
                anagram_patterns[anagram_key].append(word)
            else: 
                anagram_patterns[anagram_key] = [word]

        return list(anagram_patterns.values())