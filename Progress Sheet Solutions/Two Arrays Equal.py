class Solution:
    def checkEqual(self, a, b) -> bool:
        #code here
        a.sort()
        b.sort()
        
        if len(a)!=len(b):
            return False
        
        for i,j in zip(a,b):
            if (i!=j):
                return False
        return True
