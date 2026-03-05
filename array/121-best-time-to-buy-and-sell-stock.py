class Solution:
    def stockBuySell(self, nums, n):
        # naive: try every possible pair of days 
            # i for the buying date, check profit from i+1 ~ len(arr). 
            # time: O(n^2), space:O(1)

        # track the min price so far while traversing the arr and calculate the profit if we sell today
            # calculate profit
                # if profit > max_profit: update max
                # if current_price < min_price: update min
            # time O(n), space O(1)


        
        # arr = [10, 7, 5, 8, 11, 9]
                # min_price = nums[0] = 10, 7, 5
                # max_profit = 6
        # min_price = nums[0]
        # max_profit = 0
        # for i in range(1, len(nums)):
        #     profit = nums[i] - min_price
        #     if profit > max_profit:
        #         max_profit = profit
        #     if nums[i] < min_price:
        #         min_price = nums[i]
        # return max_profit

        min_price = float("inf")
        max_profit = 0
        for price in nums:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price-min_price)
        return max_profit

