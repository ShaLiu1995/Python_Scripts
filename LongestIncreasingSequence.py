class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        
        f = [1 for i in range(len(nums))]
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    f[i] = max(f[i], f[j] + 1)
        
        return max(f)

    # nlog(n)
    def lengthOfLIS2(self, nums):
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) / 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            size = max(i + 1, size)
        return size

if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print Solution().lengthOfLIS(nums)
    print Solution().lengthOfLIS2(nums)
        
        