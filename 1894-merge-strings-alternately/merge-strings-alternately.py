class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s=''
        i=0
        while i < max(len(word1),len(word2)):
            try:
                s=s+word1[i]
            except:
                pass
            print(s)
            try:
                s=s+word2[i]
            except:
                pass
            print(s)
            i=i+1
        return s


        