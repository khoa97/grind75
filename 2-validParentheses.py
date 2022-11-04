class Solution:
    def isValid(self, s: str) -> bool:
        stack  = []
        
        left = {"]", ")", "}"}
        right = {"[", "(", "{"}
       
        matches = { "]" : "[", 
                ")": "(",
                "}": "{"
              }
        
        for p in s:
            if p in left and len(stack) == 0:
                return False
            elif p in right:
                stack.append(p)
            else:
                cur = stack.pop()
                if matches[p] != cur:
                    return False
        return len(stack) == 0