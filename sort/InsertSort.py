# @title: InsertSort
# @description: TODO
# @author  Rhett
# @date 2022/4/6 14:49
from typing import List


class InsertSort:
    def sortArray(self,nums:List[int])->List[int]:
        n=len(nums)
        for i in range(1,n):
            tmp=nums[i]
            j=i
            while j>0 and nums[j-1]>tmp:
                nums[j]=nums[j-1]
                j-=1
            nums[j]=tmp
        return nums
    def sortArray1(self,nums:List[int])->List[int]:
        n = len(nums)
        for i in range(1,n):
            tmp=nums[i]
            j=i
            while j>0 and nums[j-1]>tmp :
                nums[j]=nums[j-1]
                j -= 1
            nums[j]=tmp

        return nums
    def sortArray2(self,data):
        for i in range(1,len(data)):
            value= data[i]
            j=i-1

            while j>=0:
                if data[j]>value:
                    data[j+1]=data[j]
                else :
                    break
                j-=1
            data[j+1]=value
        return data


if __name__=='__main__':
    a=[20,10,30,50,40,60]
    b=InsertSort().sortArray(a)
    print(b)