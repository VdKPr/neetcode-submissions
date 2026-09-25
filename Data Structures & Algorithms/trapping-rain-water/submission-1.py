class Solution:

    def trap(self, height: List[int]) -> int:

        total = 0
        left_max = 0

        # First calculate/store the maximum
        # to the left of each position
        left = [0] * len(height)

        for i in range(len(height)):
            left_max = max(left_max, height[i])
            left[i] = left_max

        right_max = 0

        # Scan from right and calculate water
        for i in range(len(height) - 1, -1, -1):

            right_max = max(right_max, height[i])

            water = min(left[i], right_max) - height[i]

            total += water

        return total