class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Detect that it is a linked list cycle program with floyd's algorithm
        # Phase 1: start at zero(both fast & slow). Iterate until they intersect
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # Phase 2: Then start both slow and interate until they intersect and return anyone
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow


        # HASHSET SOLUTION
        # hashset = set()
        # for num in nums:
        #     if num in hashset:
        #         return num
        #     hashset.add(num)