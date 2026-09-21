class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        result = set()

        for i in range(len(nums)):

            seen = set()

            for j in range(i + 1, len(nums)):

                needed = -(nums[i] + nums[j])

                if needed in seen:
                    result.add((nums[i], needed, nums[j]))

                seen.add(nums[j])

        return [list(triplet) for triplet in result]