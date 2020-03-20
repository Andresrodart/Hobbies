class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        if len(L) == 0: return 0
        maxNum = max(L)
        return self.binary(k, L, 1, maxNum)
    def binary(self, k, L, minNum, maxNum):
        mid = int((maxNum + minNum)/2)
        if minNum > maxNum or mid == 0: return 0
        res = 0
        for block in L:
            res += int(block/mid)
        if res >= k : return max(mid, self.binary(k, L, mid + 1, maxNum))
        else: return self.binary(k, L, minNum, mid - 1)
print(Solution().woodCut([232,124,456], 7))
print(Solution().woodCut([], 7))
print(Solution().woodCut([511,877,644,610,919,5734,148,968,672,637,971,501,305,152,437,446,201,464,312,163,302,2392,7431,876,978,995], 128))
print(Solution().woodCut([2147483644,2147483645,2147483646,2147483647], 4))