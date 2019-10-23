"""Doing leetcode.com problems for arrays."""

class Solution:

    def twoSum(self, nums: [int], target: int) -> [int]:
        """This method will take a list of integers as input, and a target,
        and return indices of two numbers such that their sum is target.
        NOTE: there is exactly one solution, and there are no duplicates
        in the input list."""
        index_map = {} # initialize hashmap with key = number, value = index
        for i in range(len(nums)): # iterate thru minuends
            subtrahend = target - nums[i] # calculate subtrahend
            if subtrahend in index_map: # look in hashmap for subtrahend
                return [index_map[subtrahend], i] # return indices of minuend and subtrahend
            index_map[nums[i]] = i # update hashmap

    def maxProfit(self, prices: [int]) -> int:
        """This method will take a list of stock prices, and return the maximum
        profit from buying and selling. If 0 profit exists, return that."""
        profit = 0
        if prices != []: # Check to make sure prices isnt empty.
            buy = prices[0] # assign temporary buy price to first day
        for i in range(len(prices)):
            if prices[i] < buy: # compare potential new buy with current buy
                buy = prices[i]
            elif (prices[i] - buy > profit): # if the buy was higher, compare sell - buy with profit.
                profit = prices[i] - buy
        return profit



# print(Solution().maxProfit([7,1,5,3,6,4]))
# print(Solution().maxProfit([7,6,4,3,1]))



