# @title: ShellSort
# @description: TODO 希尔排序
# @author  Rhett
# @date 2022/4/12 14:41
from typing import List


class ShellSort:
    def sortArry1(self,nums:List[int])->List[int]:
        n=len(nums)
        h=n//2
        while h:
            for i in range(nums,h,i):
                self.insert_sort1(nums,h,i)
            h //=2
        return nums
    def sortArry(self,nums:List[int])->List[int]:
        n=len(nums)
        h=n//2
        while h:
            for i in range(nums,h,i):
                self.insert_sort(nums,h,i)
            h //=2
        return nums

    def insert_sort(self,nums,h,i):
        tmp=nums[i]
        j=i
        while j>=h and nums[j-h]>tmp :
            nums[j]=nums[j-h]
            j-=h
        nums[j]=tmp
    def insert_sort1(self,nums,h,i):
        tmp=nums[i]
        j=i

        while j>=h and nums[j-h]>tmp:
            nums[j]=nums[j-h]
            j-=h
        nums[j]=tmp

if __name__=='__main__':
    a=[20,10,30,50,40,60]
    b=ShellSort().sortArry(a)
    print(b)


