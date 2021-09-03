# @title: TwoSum
# @description: TODO 简单的题型 只是计算2个数之和 返回一个数组
# @author  Rhett
# @date 2021/8/30 11:27
from typing import List

from algo import ListNode


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

    def twoSum3(self,l1:ListNode,l2:ListNode)->ListNode:
        #首先创建一个虚拟节点，并创建一个current指针，指向这个节点
        current=dummy=ListNode()
        carry,value=0,0
        while carry or l1 or l2:
            value=carry

            if l1:l1,value=l1.next,l1.val+value
            if l2:l2,value=l2.next,l2.val+value

            carry,value=divmod(value,10)
            current.next=ListNode(value)
            current=current.next
        return dummy.next