class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # naive: use set to get all unique number, and 
        # non-decreasing order
        # two pointers
        # slow pointer i bulid anwser, for unque element position
        # faster pointer j scan input. for each nums, check if nums[j] == nums[i], if not place to i and move on the the next, if it is duplicate, skip
        if not nums:
            return 

        i = 0 # last uniqe element
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1
        # time: O(N), space: O(1)