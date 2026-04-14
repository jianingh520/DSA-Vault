"""
Problem Statement: 

Given an array/list of length ‘N’, where the array/list represents \
the boards and each element of the given array/list represents the length of each board. 
Some ‘K’ numbers of painters are available to paint these boards. 
Consider that each unit of a board takes 1 unit of time to paint. 
You are supposed to return the area of the minimum time to get this job done of painting all the ‘N’ boards 
	under the constraint that any painter will only paint the continuous sections of boards.

Example 1:
Input Format: N = 4, boards[] = {5, 5, 5, 5}, k = 2
Result: 10
Explanation: We can divide the boards into 2 equal-sized partitions, so each painter gets 10 units of the board and the total time taken is 10.

Example 2:
Input Format: N = 4, boards[] = {10, 20, 30, 40}, k = 2
Result: 60
Explanation: We can divide the first 3 boards for one painter and the last board for the second painter.
            
"""


class PainterPartition:
    # count painters required for a given max allowed time
    def count_painters(self, boards: List[int], time: int) -> int:
        painters = 1 # always start with at least 1 painter
        boards_painter = 0 # how much work the current painter has taken

        for board in boards:
            if boards_painter + board <= time:
                boards_painter += board
            else:
                painters += 1
                boards_painter = board

        return painters

    # use binary search to find the minimum time
    def find_min_time(self, boards: List[int], k: int) -> int:
        low = max(boards)
        high = sum(boards)
        res = high

        while low <= high:
            mid = (low + high) // 2
            painters = self.count_painters(boards, mid)

            if painters > k:
                low = mid + 1  # too many painters needed, increase time
            else:
                res = mid   # valid time, try reducing time
                high = mid - 1

        return res

# Test
boards = [10, 20, 30, 40]
k = 2
pp = PainterPartition()
ans = pp.find_min_time(boards, k)
print("The answer is:", ans)  # Expected: 60