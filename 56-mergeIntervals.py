class Solution(object):

    # Time Complexity: O(nlogn)
    # Space Complexity: O(n)

    # Approach: Sorting
    # 1. Sort the intervals by the start time
    # 2. Initialize an empty list called merged
    # 3. Iterate over the intervals
    # 4. If the merged list is empty or if the current interval does not overlap with the previous, append it.
    # 5. If there is an overlap, merge the current interval with the previous one
    # 6. Return the merged list

    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # First, sort the intervals by the start time
        intervals.sort(key=lambda interval: interval[0])

        merged = []

        for interval in intervals:
            # If the merged list is empty or if the current interval does not overlap with the previous, append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # If there is an overlap, merge the current interval with the previous one
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged