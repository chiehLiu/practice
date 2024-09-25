class Solution:
    # Time: O(nlogn)
    # Space: O(n)

    # this one is hard, need more grinding

    # sort the cars by position
    # iterate through the cars from the end
    # calculate the time to reach the target
    # if the time is less than the time of the car in front of it, then it will be in the same fleet, so pop the last car
    # if the time is greater than the time of the car in front of it, then it will be in a new fleet
    # return the length of the stack
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        stack = []
        pair.sort(reverse=True)

        for p, s in pair:
            stack.append((target - p) / s)

            # we don't need while loop since we already pop the faster car in former iteration
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)