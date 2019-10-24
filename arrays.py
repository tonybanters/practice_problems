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
    
    def containsDuplicate(self, nums: [int]) -> bool:
        """This method will return true if the list contains 1 element at least twice,
        and return false if every element is unique."""
        # ... really simple, remove dupes and see if lists are equal length.
        """ temp = list(set(nums))
            return len(temp) != len(nums) """
        # but this will not be O(n) in worst case, it will be every case O(n)
        # can make small improvement, for average case, by iterating the set while making it
        # and breaking the loop if set contains dupe
        temp = set()
        for number in nums:
            if number in set:
                return True
            set.add(number)
        return False
        # for some reason this is slower, maybe for smaller lists. not sure, need to look into it


    def productExceptSelf(self, nums: [int]) -> [int]:
        """This method will take a list of ints as input, and return a list of
        products of the list, excluding the ith index, without using division, in O(n) time"""
        result = []
        left = [1]*len(nums)
        right = [1]*len(nums)
        for i in range(1,len(nums)):
            left[i] = left[i-1] * nums[i-1]
        for i in reversed(range(len(nums)-1)):
            right[i] = right[i+1] * nums[i+1]
        for i in range(len(nums)):
            result.append(left[i]*right[i])
        return result



