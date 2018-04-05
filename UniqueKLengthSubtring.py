class Solution(object):
    def UniqueKLengthSubstring(self, s, k):
        """
        :type nums: List[int]
        :rtype: int
        """
        if s is None or len(s) == 0:
            return []
        
        ans = []
        
        for i in range(len(s) - k + 1):
            substr = s[i: i + k]
            # print "all " + substr
            if substr not in ans:
                # print substr
                ans.append(substr)

        
        return sorted(ans)

    

if __name__ == "__main__":
    s = "caaab"
    k = 2
    print Solution().UniqueKLengthSubstring(s,k)
        
        