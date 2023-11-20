
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
    

#%% https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        equation to maximize: area = (r-l) * min(height[r],height[l])
        Maximize both factors.
        (r-l) is maximal with l=0, r = len(height)-1
        -> that's where we start and initialize our pointers to
        Now find a way to smoothly decrease (r-l) while always retaining the maximal height possible.
        '''
        mx = 0
        l = 0
        r = len(height)-1
        while l<r:
            print(l,r)
            mx = max(mx, (r-l) * min(height[r],height[l]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return mx

        # # Brute force
        # mx = 0
        # for r in range(len(height)):
        #     for l in range(r):
        #         cur = (r-l) * min(height[r],height[l])
        #         #print(r, l, min(height[r],height[l]), mx)
        #         if cur > mx:
        #             mx = cur
        # return mx


#%% https://app.codesignal.com/interview-practice/question/rMe9ypPJkXgk3MHhZ/description

def solution(coins, quantity):
    # Generate a set of with unique sum results by adding a single coin to all previous results
    res = {0}
    for c, q in zip(coins, quantity):
        res  = {
            r + c * i for r in res for i in range(q+1)
        }
    return len(res) -1