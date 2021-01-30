##
# @ description: TODO 三角形最短路径和 动态规划 dp[i][j]=min(dp[i+1][j],dp[i+1][j+1])+triangle[i][j]
# @ author Rhett.wang
# @ date 2020 / 8 / 30 20: 01
#
from typing import List
class MinPathSum:
    def minimumTotal(self,triangle:List[List[int]])->int:
        dp=triangle[-1]
        for i in range(len(triangle)-2,-1,-1):
            for j in range(i+1):
                dp[j]=triangle[i][j]+min(dp[i],dp[j+1])
        return dp[0]

if __name__ == '__main__':
    so= MinPathSum