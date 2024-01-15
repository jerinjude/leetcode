class Solution:
    def romanToInt(self, s: str) -> int:
        diction={'I':1,
              'V':5,
              'X':10,
              'L':50,
              'C':100,
              'D':500,
              'M':1000}
        sum=0
        for i,j in enumerate(s[:-1]):
            if diction[s[i+1]]<=diction[s[i]]:
                sum=sum+diction[j]
            else:
                sum=sum-diction[j]
            print(sum)

        return sum + diction[s[-1]]