class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]*(n+1)
        zero = 1
        for i in range(1, n+1):
            if i == zero*2:
                zero = i
            dp[i] = dp[i-zero] + 1
        
        return dp