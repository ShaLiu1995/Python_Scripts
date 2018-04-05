# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 16:14:45 2017

@author: sand
"""

class Solution(object):
    def numberSquareDP(self, nums):
        """
        :type nums: list[list[int]]
        :rtype: int
        """
        N = len(nums)
        P = 2 * N - 2
        dp = [[[0 for i in xrange(N)] for j in xrange(N)] for k in xrange(N * 2)]
        
        for i in range(N):
            for j in range(N):
                dp[0][i][j] = -1
                
        dp[0][0][0] = nums[0][0]
        
        for s in range(1, P + 1):
            for i in range(N):
                for j in range(i, N):
                    dp[s][i][j] = -1
                    if not self.isValid(s, i, j, nums):
                        continue
                    dp[s][i][j] = max(dp[s][i][j], self.getValue(s - 1, i - 1, j - 1, nums, dp))
                    dp[s][i][j] = max(dp[s][i][j], self.getValue(s - 1, i - 1, j    , nums, dp))
                    dp[s][i][j] = max(dp[s][i][j], self.getValue(s - 1, i    , j - 1, nums, dp))
                    dp[s][i][j] = max(dp[s][i][j], self.getValue(s - 1, i    , j    , nums, dp))
                    if i != j:
                        dp[s][i][j] += nums[i][s - i] + nums[j][s - j]     
                    else:
                        dp[s][i][j] += nums[i][s - i]
        
        return dp[P][N - 1][N - 1]

    def isValid(self, s, x1, x2, nums):
        n = len(nums)
        y1 = s - x1
        y2 = s - x2
        if nums[x1][x2] == -1:
            return False
        elif x1 < 0 or x1 >= n:
            return False
        elif x2 < 0 or x2 >= n:
            return False
        elif y1 < 0 or y1 >= n:
            return False
        elif y2 < 0 or y2 >= n:
            return False
        else:
            return True
        
    def getValue(self, s, x1, x2, nums, dp):
        if self.isValid(s, x1, x2, nums):
            return dp[s][x1][x2]
        else:
            return -1
        
        
if __name__ == "__main__":
    nums = [[1,2,2,1,3,3] for i in range(6)]
    ans = Solution().numberSquareDP(nums)
    print ans