class Solution:
    def isValid(self, s: str) -> bool:
        # Check if the string is even - as every opening has a closing
        if len(s)%2 !=0:
            return False
        
        # Using Hash Map for opening/closing pairs
        bracket_map = {
            '}':'{', 
            ']':'[',
            ')':'('
            }
        
        stack = []

        for char in s:
            if char in bracket_map:

                # Pop the top element if stack isnt empty, otherwise a dummy variable
                top_element = stack.pop() if stack else '#'

                if bracket_map[char] != top_element:
                    return False
            
            else:
                # Add to stack if it is an opening bracket
                stack.append(char)
        
        # Return True if stack is completely empty in the end
        return not stack
        