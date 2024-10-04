class Solution:
    # Time: O(log(min(m, n)))
    # Space: O(1)

    # not dont yet
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # A is shorter, B is longer keep that in mind 
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        # make sure A is the shorter one
        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            
            # i is the A mid index temporarily
            i = (l + r) // 2

            # since i is the temp one half in A
            # so j is the other half, (half - i) would be the portion of B
            # and why -2? because "half" is length and we compare index here so we need to -1 on A and -1 on B
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1