class Solution:
    def isValid(self, s: str) -> bool:
        stack1 = []

        if len(s) % 2 != 0:
            return False
        for char in s:
            if char in ('(','[', '{'):
                stack1.append(char)
            elif char == ')':
                if not stack1 or stack1[-1] != '(' :
                    return False
                else:
                    stack1.pop()
            elif char == ']':
                if not stack1 or stack1[-1]!= '[' :
                    return False
                else:
                    stack1.pop()
            elif char == '}':
                if not stack1 or stack1[-1]!='{' :
                    return False
                else:
                    stack1.pop()
            else:
                return False
        if not stack1:
            return True
        else:
            return False
        
