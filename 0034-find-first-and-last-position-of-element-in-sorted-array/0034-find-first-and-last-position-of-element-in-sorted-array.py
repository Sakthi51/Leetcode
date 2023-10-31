class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # check target is in the array
        if target not in nums:
            return [-1, -1]

        # loop from the begining
        index_of_first = 0
        for i in range(len(nums)):
            if nums[i] == target:
                index_of_first = i
                break

        # loop from the last
        index_of_last = 0
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == target:
                index_of_last = i
                break

        return [index_of_first, index_of_last]

# Time complexity - O(n)
# Space complexity - O(n)

        