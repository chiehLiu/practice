class Solution:
    # Time: O(2n) => O(n)
    # Space: O(n)

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            else:
                # Truncation (with int()): It simply cuts off the decimal part, 
                # floor() rounds down to the nearest integer.
                stack.append(int(c))
        
        return stack[0]