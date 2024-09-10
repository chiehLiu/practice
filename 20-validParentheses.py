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
    


    class Solution:
        def isValid(self, s: str) -> bool:
            if len(s) % 2 != 0:
                return False
            
            hash_map = {
                "}": "{",
                ")": "(",
                "]": "["
            }

            stack = []

            for p in s:
                # meet the closing tag
                if p in hash_map:

                    # this is no opening tag only closing tag in the input
                    if not stack and hash_map[p]:
                        return False
                    # this is something already in the stack and the latest closing tag does not matching the opening tag at the end of the stack
                    if stack and stack[-1] != hash_map[p]:
                        return False
                    
                    # something in the stack and the closing tag matched the opening at the end of the stack
                    if stack and stack[-1] == hash_map[p]:
                        stack.pop()

                # for opening tag pushing to stack
                else:
                    stack.append(p)
            
            return len(stack) == 0
