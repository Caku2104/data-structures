# LeetCode 'First Unique Character in a String' Problem 

class Solution(object):
    def firstUniqChar(self, s):
        counter = {}
        for ch in s:
            if not ch in counter:
                counter[ch] = 0
            counter[ch] += 1

        for i, ch in enumerate(s):
            if counter[ch] == 1:
                return i
        return -1    
