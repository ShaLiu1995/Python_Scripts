class Solution:
    """
    @param {int} n a integer
    @return {int} a integer
    """
    def countPairs(self, n):
        # write your code here
        if n <= 1:
            return 1
            
        if n == 2:
            return 2

        a, b, c = 1, 1, 2
        for i in xrange(3, n + 1):
            a, b, c = b, c, a + b + c

        return c

if __name__ == "__main__":
    n = 3
    print Solution().climbStairs2(n)