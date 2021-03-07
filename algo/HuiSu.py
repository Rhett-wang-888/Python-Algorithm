# @title: HuiSu
# @description: TODO 字符串回文分割 使用回溯方法 这个方法就是使用字符关系
# @author  Rhett
# @date 2021/3/7 14:28
from typing import List


class Solution:
    def partition(self,s:str)->List[List[str]]:
        n =len(s)
        f=[[True]*n for _ in range(n)]

        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                f[i][j]=(s[i]==s[j]) and f[i+1][j-1]
        ret =list()
        ans=list()
        def dfs(i:int):
            if i==n:
                ret.append(ans[:])
                return
            for j in range(j,n):
                if f[i][j]:
                    ans.append(s[i:j+1])
                    dfs(j+1)
                    ans.pop()
        dfs(0)
        return ret
