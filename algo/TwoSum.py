# @title: TwoSum
# @description: TODO 简单的题型 只是计算2个数之和 返回一个数组
# @author  Rhett
# @date 2021/8/30 11:27
from typing import List


class TwoSum:
    def twoSum1(self,nums:List[int],target:int)->List[int]:
        n =len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return []

    def twoSum2(self,nums:List[int],target:int)->List[int]:
        hash=dict()
        for i,num in enumerate(nums):
            if target-num in hash:
                return [hash[target-num],i]
            hash[nums[i]]=i
        return []