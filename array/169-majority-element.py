class Solution:
    def majorityElement(self, nums):
        # for each element, count # of freq 
            # time O(n^2)
        # A straightforward approach is to count frequencies using a hash map, which would take O(n) time and O(n) space.
            # time O(n), space O(n)
        # opt: However, the majority element appears more than half the time, it must outnumber all other elements combined. That suggests we can cancel out different elements.
            #So I’ll maintain a candidate and a counter. If the counter is zero, I select the current number as the new candidate. If the number matches the candidate, I increment the counter. Otherwise, I decrement the counter.
            # Intuitively, different elements cancel each other out, and since the majority element appears more than all others combined, it will remain as the final candidate."
 
        

        # freq = {}
        # for num in nums:
        #     freq[num] = 1 + freq.get(num, 0)

        # n = len(nums)
        # for k, v in freq.items():
        #     if v > n//2:
        #         return k
        # return -1

        # Boyer–Moore voting 
            # time O(n), space O(1)

        candidate = None
        cnt = 0
        for i in range(len(nums)):
            if cnt == 0:
                candidate = nums[i]            
            if nums[i] == candidate:
                cnt += 1
            else:
                cnt -= 1
        return candidate
    