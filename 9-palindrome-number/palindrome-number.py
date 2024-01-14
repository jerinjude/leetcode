class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        n = len(x_str)
        flag = True
        
        if n % 2 == 0: 
            for i in range(n // 2):    
                if x_str[i] == x_str[n - i - 1]:
                    continue
                else:
                    flag = False
        else:
            for i in range(n // 2):    
                if x_str[i] == x_str[n - i - 1]:
                    continue
                else:
                    flag = False
        
        return flag


            
        