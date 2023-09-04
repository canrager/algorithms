
from typing import List
#%% https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = prices[0]
        profit = [0]
        for i in range(1, len(prices)):
            profit.append(prices[i] - mn)
            if mn > prices[i]: # faster than min(mn, prices[i])
                mn = prices[i]
        return max(profit)
    

#%% https://leetcode.com/problems/maximum-subarray/submissions/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        Traverse array once with running sum. Keep track of most negative contiguous sum starting at the beginning. max_subarray = max(running_sum - most negative sum).
        O(n) Time complexity: Iterate through for loop once. Math operations and array information retrieval are O(1).
        '''
        most_negative_sum = 0
        running_sum = 0
        max_sum = nums[0]
        for i in range(len(nums)):
            running_sum += nums[i]
            subarray_sum = running_sum - most_negative_sum
            if subarray_sum > max_sum:
                max_sum = subarray_sum
            if running_sum < most_negative_sum:
                most_negative_sum = running_sum
        return max_sum