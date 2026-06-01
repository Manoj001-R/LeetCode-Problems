class Solution:
    def isPalindrome(self, x: int) -> bool:
        string=str(x)
        reverse_str=string[::-1]

        for i in range(len(string)):
            if string==reverse_str:
                return True 
            else:
                return False
            