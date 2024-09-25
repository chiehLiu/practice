class Solution:
    
    # Time: O(n)
    # Time: O(n)

    # this one is hard, need more grinding
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # if you meet the biggest temp, the 0 will fill the result since there is no warmer temp
        res = [0] * len(temperatures) 
        stack = [] # pair: [temp, index]

        for i, t in enumerate(temperatures):
            # if the current temp i greater than the last temp in the stack and stack is not empty
            while stack and t > stack[-1][0]:
                # pop the last temp and index
                stackT, stackI = stack.pop()

                # calculate the difference between the current index and the last index
                res[stackI] = i - stackI

            # append the current temperature and index
            stack.append([t, i])
        return res                