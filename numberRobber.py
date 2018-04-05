# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 15:32:27 2017

@author: sand
"""

class Solution(object):
    def numberRobber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numDict = {}
        for i in nums:
            numDict[i] = numDict.get(i,0) + 1
         
        maxNum = max(nums)   
        dp = [0] * (maxNum + 1)
        dp[1] = 1 * numDict[1]
        dp[2] = 2 * numDict[2]
        for i in range(3, len(dp)):
            dp[i] = max(dp[i-1], dp[i-2] + i * numDict.get(i,0))
        
        return dp[maxNum]

if __name__ == "__main__":
    nums = [1,2,2,1,3,3]
    ans = Solution().numberRobber(nums)
    print ans