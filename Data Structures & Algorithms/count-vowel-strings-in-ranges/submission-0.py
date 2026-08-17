class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        def sats(word):
            return word[0] in vowels and word[-1] in vowels
        
        pref = [0]
        for i in range(0, len(words)):
            pref.append(pref[-1] + 1 if sats(words[i]) else pref[-1])
        
        return [pref[q[1]+1] - pref[q[0]] for q in queries]

