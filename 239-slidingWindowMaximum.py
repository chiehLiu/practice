# import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque() # stores indices
        l = r = 0

        while r < len(nums):
            # Remove smaller elements from queue rear
            # we are maintaining decreasing order in the queue so that we can get the maximum element at the front
            while q and nums[r] > nums[q[-1]]:
                q.pop()

            # if the current ele(num[r]) is less than the last ele in the queue, add it to the queue
            q.append(r)

            if l > q[0]:
                q.popleft()
            
            # r + 1 is the length of it
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            
            r += 1
        
        return output