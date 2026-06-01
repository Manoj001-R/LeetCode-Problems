class Solution:
    def isValid(self, s: str) -> bool:
       stack=[]
       match={')':'(','}':'{',']':'['}
       opening=set('({[')

       for char in s:
        if char in opening:
            stack.append(char)
        elif char in match:
            if not stack:
                return False 
            if stack[-1] != match[char]:
                return False 

            stack.pop()
        
       return len(stack)==0