class Solution(object):
    
    # O(n) time complexity
    # O(n) space complexity
    
    #using a stack and a dictionary to keep track of the opening and closing brackets.
    
    # The idea is to use a stack to keep track of the opening brackets.
    # If we encounter a closing bracket, we check if the top of the stack is the corresponding opening bracket.
    # If it is, we pop the opening bracket from the stack and continue.
    # If it is not, we return False.
    # If the stack is empty at the end, we return True.
    
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lookup ={
            "(": ")",
            "[": "]",
            "{": "}"
            }
        stack = []
        
        for char in s:
            if char in lookup:
                stack.append(char)
            elif not stack or char != lookup[stack.pop()]:
                return False
        
        return len(stack) == 0