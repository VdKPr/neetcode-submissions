class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        n = len(nums)
        result = []

        for i in range(n - 2):

            a = nums[i]

            if i > 0 and a == nums[i - 1]:
                continue

            # Since a is the smallest number,
            # nothing after this can make a valid triplet.
            if a > 0:
                break

            # Smallest possible sum is too large.
            if a + nums[i + 1] + nums[i + 2] > 0:
                break

            # Largest possible sum is too small.
            if a + nums[n - 2] + nums[n - 1] < 0:
                continue

            left = i + 1
            right = n - 1

            while left < right:

                total = a + nums[left] + nums[right]

                if total < 0:
                    left += 1

                elif total > 0:
                    right -= 1

                else:
                    result.append([a, nums[left], nums[right]])

                    left_value = nums[left]
                    right_value = nums[right]

                    while left < right and nums[left] == left_value:
                        left += 1

                    while left < right and nums[right] == right_value:
                        right -= 1

        return result