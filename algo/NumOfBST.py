# @title: NumOfBST
# @description: TODO
# @author  Rhett
# @date 2020/7/15 9:07 1到n个数据 计算所有的二叉搜索树个数

class solution:
    def numTree(self,n):
        G=[0]*(n+1)
        G[0],G[1]=1,1
        for i in range(2,n+1):
            for j in range(0,i):
                G[i] +=G[j]*G[i-j-1]
        return G[-1]

    