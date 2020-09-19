# @title: SwapPairs
# @description: TODO 盛最多水的 容器
# @author  Rhett
# @date @date 2020/9/19 21:16
from typing import List

class Solution:
    def maxArea(self,height:List[int])->int:
        l,r=0,len(height) -1
        ans=0
        while l<r:
            area=min(height[l],height[r])*(r-l)
            ans=max(ans,area)
            if height[l] <= height[r]:
                l+=1
            else:
                r -=1
        return ans