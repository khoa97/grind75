class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        bucket = [0] * 26
        
        for c in s:
            bucket[ord('a')-ord(c)] += 1
            
        
        for c in t:
            bucket[ord('a') -  ord(c)] -=1
        
        for i in bucket:
            if i != 0:
                return False
        
        return True