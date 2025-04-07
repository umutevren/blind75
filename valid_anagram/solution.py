from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s= s.lower()
        t= t.lower()
        
        if sorted(s)== sorted(t):
            return True
        else:
            return False 