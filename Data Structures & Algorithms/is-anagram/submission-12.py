class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        
        visitedS, visitedT = {}, {}

        for i in range(len(s)): 
            visitedS[s[i]] = 1 + visitedS.get(s[i], 0)
            visitedT[t[i]] = 1 + visitedT.get(t[i], 0)
        return visitedS == visitedT
        