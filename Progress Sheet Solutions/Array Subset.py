#User function Template for python3
from collections import Counter
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        # for i in b:
        #     if i not in a:
        #         return False
        # return True
        
        aDict = Counter(a)
        bDict = Counter(b)
    
        for k,v in bDict.items():
            if (k not in aDict.keys() or  aDict[k] < v):
                return False
                
        return True
