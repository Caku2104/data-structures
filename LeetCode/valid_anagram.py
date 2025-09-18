
# 'Valid Anagram' Problem

class Solution(object):
    def isAnagram(self, s, t):
        chars = {}
        comparison = {}

        for ch in s:
            if not ch in chars:
                chars[ch] = 1
            else:
                chars[ch] += 1
        
        for ch in t:
            if not ch in comparison:
                comparison[ch] = 1
            else:
                comparison[ch] += 1
            
        if chars == comparison:
            return True
        return False