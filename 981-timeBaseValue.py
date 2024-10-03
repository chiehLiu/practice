from collections import defaultdict

# Time: O(1) for set, O(logn) for get
# Space: O(n)
class TimeMap:

    def __init__(self):
        # self.store = {} # key: list of [val, timestamp]
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # if key not in self.store: 
        #     self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""

        # if not using defaultdict
        # value = self.store.get(key, [])
        value = self.store[key]

        l, r = 0, len(value) - 1

        while l <= r:
            m = (l + r) // 2

            if value[m][1] <= timestamp:
                # each value smaller than timestamp is a candidate
                # so we keep adding until the while loop ends, which means we find the closest one
                res = value[m][0]
                l = m + 1
            else:
                r = m - 1
        
        return res

# The // operator in Python is used for integer (or floor) division.
# the result is "floored" to the nearest integer.

# # Integer division
# print(10 // 3)    # Output: 3 (because 10 ÷ 3 = 3.33, but the floor is 3)
# print(20 // 4)    # Output: 5 (because 20 ÷ 4 = 5, and it's already an integer)

# # Division with negative numbers
# print(-10 // 3)   # Output: -4 (because the result is floored to the next lower integer)

# # Float division (but still returns a floored value)
# print(10.5 // 3)  # Output: 3.0 (because 10.5 ÷ 3 = 3.5, but the floor is 3.0)
# print(10 // 3.0)  # Output: 3.0 (same as above, but with one operand as float)

# # Negative float division
# print(-10.5 // 3) # Output: -4.0 (because it floors down to -4.0)
