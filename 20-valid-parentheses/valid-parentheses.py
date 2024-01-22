class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        dicti={')':'(',
              ']':'[',
              '}':'{'}
        if s[-1] in dicti.values() or s[0] in dicti.keys():
            return False
        for c in s:
            if c in dicti:
                if l and l[-1]==dicti[c]:
                    l.pop()
                else:
                    return False 
            else:
                l.append(c)
        if not l:
            return True
        else:
            return False
                




