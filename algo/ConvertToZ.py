# @title: ConvertToZ
# @description: TODO
# @author  Rhett
# @date 2021/9/3 9:49

class zonvertToZ:
    def convert(self,s:str,numRows:int)->str:
        if numRows<2:return s
        res=["" for _ in range(numRows)]

        i,flag=0,-1
        for c in s:
            res[i] +=c
            if i==0 or i==numRows-1:flag=-flag
            i +=flag

        return "".join(res)
