from itertools import permutations
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequency_s={}
        frequency_t={}
        # key: char, value=frequency
        for char in s:
            frequency_s[char]=frequency_s.get(char,0)+1

        for char in t:
            frequency_t[char]=frequency_t.get(char,0)+1
        
        if frequency_s==frequency_t:
            return True
        else:
            return False